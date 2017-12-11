# coding=utf8

import requests
import functools
import argparse
from lxml import etree
from user_agent import generate_user_agent
import os
import re
import json
from random import choice
import codecs

LEVEL_DICT = {1: 'easy', 2: 'medium', 3: 'hard'}
TOP_ELEMENT = u'-'
LEFT_ELEMENT = u'|'

FILE_SUFFIX_DICT = {'python': 'py'}


def clear_pagedate_value(value):
    if value.startswith('[') and value.endswith('],'):
        value = value.replace("'", '"')
        value = value[:-3] + ']'
        return json.loads(value)
    else:
        m = re.findall(r"'([^']+)',?", value)
        if len(m) == 1:
            return m[0]
        else:
            return False


def clear_pagedata_line(line):
    try:
        linelist = line.split(': ')
        if len(linelist) < 2:
            return False
        elif len(linelist) == 2:
            key = linelist[0].strip()
            value = linelist[1]
        else:
            key = linelist[0].strip()
            value = ': '.join(linelist[1:])
        value_clear = clear_pagedate_value(value)
        if value_clear:
            return [key, value_clear]
    except Exception as e:
        print(e)
    return []


def clear_pagedata(pagedata):
    pageDatalist = [i for i in pagedata.split('\n') if i and ': ' in i]
    result = {}
    for line in pageDatalist:
        r = clear_pagedata_line(line)
        if not r:
            continue
        result.update({r[0]: r[1]})
    return result


def create_leetcode_exercise(name, description, codeDefinition, difficulty='easy', language='python'):
    content = []
    if language.lower() == 'python':
        content.append('# coding = utf8')
        content.append('"""%s"""' % description)
        content.append(codeDefinition)
        content.extend(['', 'if __name__ == "__main__":', '    inputs = ""', '    sol = Solution()'])
        filename = name + '.' + FILE_SUFFIX_DICT[language]
        filefullpath = os.path.join(difficulty, filename)
    if not os.path.exists(difficulty):
        os.mkdir(difficulty)
    with codecs.open(filefullpath, 'w', encoding='utf8') as f:
        for c in content:
            # if isinstance(c, str):
            # TODO python3
            try:
                # c = c.decode('unicode_escape', 'ignore')
                f.write(c + u'\n')
            except UnicodeEncodeError as e:
                print('error: ', c)
                print(e)
    print('create success: %s' % filefullpath)


def printcontents(contents):
    max_length = len(max(contents, key=lambda x: len(x)))
    show_list_after = []

    top_line = TOP_ELEMENT * (max_length + 2)
    show_list_after.append(top_line)
    for line in contents:
        line = '%s%s%s%s' % (LEFT_ELEMENT, line, ' ' * (max_length - len(line)), LEFT_ELEMENT)
        show_list_after.extend([line, top_line])
    for line in show_list_after:
        print(line)
    print('')


class CrawlException(Exception): pass


def retry(count=3):
    def deco(func):
        global timeout_count
        timeout_count = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            global timeout_count
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if timeout_count < count:
                    timeout_count += 1
                    print(u'失败第 %s 次, 错误: %s, 开始重试' % (timeout_count, e.message))
                    return wrapper(*args, **kwargs)
                else:
                    print(u'超过最大重试次数 %s 次, 结束' % count)

        return wrapper

    return deco


class LeetCodeCrawlerObject:
    def __init__(self):
        headers = {
            'User-Agent': generate_user_agent(os=('mac', 'linux')),
        }
        self.sess = requests.Session()
        self.sess.headers.update(headers)
        self.timeout = 5

    def fetch_all_problem(self):
        url_api = 'https://leetcode.com/api/problems/all/'
        r = self.sess.get(url_api, timeout=self.timeout)
        j = json.loads(r.text)
        # 打印信息
        keys_show = [u'ac_easy', u'category_slug', u'is_paid', u'frequency_high', u'frequency_mid', u'ac_medium',
                     u'num_solved', u'ac_hard', u'user_name', u'num_total']

        show_list = ['%s: %s' % (key, j[key]) for key in keys_show if key in j]
        printcontents(show_list)
        return j[u'stat_status_pairs']

    def choice_one(self, problems, **kwargs):
        language = kwargs.get('language', 'python')
        difficulty = kwargs.get('difficulty', '')
        problems_filted = [problem for problem in problems if
                           not difficulty or difficulty == LEVEL_DICT.get(problem['difficulty']['level'], '')]
        problem = choice(problems_filted)
        level = problem['difficulty']['level']
        level_dirname = LEVEL_DICT[level]
        question__title_slug = problem['stat']['question__title_slug']
        filefullpath = os.path.join(level_dirname, '%s.%s' % (question__title_slug, FILE_SUFFIX_DICT[language]))
        if os.path.exists(filefullpath):
            print(u'已经存在,重新获取...')
            self.choice_one(problems, **kwargs)
        # 打印信息
        keys = [u'question_id', u'question__title', u'total_acs', u'total_submitted', u'is_new_question']
        contents = ['%s: %s' % (key, problem['stat'][key]) for key in keys if key in problem['stat']]
        contents.append('difficulty: %s' % level_dirname)
        printcontents(contents)
        return problem

    @retry(count=3)
    def crawl_from_url(self, url, **kwargs):
        # name = url.split('problems')[-1].split('/')[0]
        res = self.sess.get(url, timeout=self.timeout)
        root = etree.HTML(res.text)
        # 难度
        difficulty = root.xpath('//span[contains(@class, "difficulty-label")]/text()')
        difficulty = difficulty[0].lower() if difficulty else 'easy'

        question_descrition_list = root.xpath('//div[@class="question-description"]//text()')
        if len(question_descrition_list) == 0:
            raise CrawlException(u'找不到问题描述')
        question_descrition = ''.join(question_descrition_list)

        # find config in script
        scripts = [i for i in root.xpath('//script') if not i.attrib and 'pageData' in i.text]
        assert len(scripts) == 1
        pageData = scripts[0].text
        pageDataDict = clear_pagedata(pageData)
        codeDefinition = pageDataDict['codeDefinition']
        code_def = [i['defaultCode'] for i in codeDefinition if i['text'].lower() == kwargs.get('language')]
        code_def = code_def[0] if code_def else ''
        create_leetcode_exercise(pageDataDict['questionTitleSlug'],
                                 question_descrition,
                                 code_def,
                                 difficulty=difficulty,
                                 language=kwargs.get('language'))

    def crawl(self, **kwargs):
        urls = kwargs.pop('url')
        if not urls:
            # random leetcode
            problem = self.choice_one(self.fetch_all_problem(), **kwargs)
            url_problem = 'https://leetcode.com/problems/%s' % problem['stat']['question__title_slug']
            print(url_problem)
            self.crawl_from_url(url_problem, **kwargs)
        else:
            for url in urls:
                self.crawl_from_url(url, **kwargs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""www.leetcode.com crawler""")
    parser.add_argument('-u', '--url', type=str, help='url of leetcode problem', nargs='*', default=None)
    parser.add_argument('-l', '--language', type=str, default="python", metavar='lang',
                        help=u'语言 code language: %s' % FILE_SUFFIX_DICT.keys())
    parser.add_argument('-d', '--difficulty', type=str,
                        help=u'难度 problem difficulty : %s' % ', '.join(LEVEL_DICT.values()))
    parser.add_argument('-a', '--answer', type=bool, default=False, help=u'是否找答案 whether find answer(TODO)')
    args = parser.parse_args()
    lcc = LeetCodeCrawlerObject()
    lcc.crawl(**args.__dict__)
