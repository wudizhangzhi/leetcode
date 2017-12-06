# coding = utf8

import requests
import argparse
from lxml import etree
from user_agent import generate_user_agent
import re
import json


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


def create_leetcode_exercise(name, description, codeDefinition, language='python'):
    content = []
    if language.lower() == 'python':
        content.append('# coding = utf8')
        content.append('"""%s"""' % description)
        content.append(codeDefinition)
        content.extend(['', 'if __name__ == "__main__":', '    inputs = ""', '    sol = Solution()'])
        filename = name + '.py'

    with open(filename, 'wb') as f:
        for c in content:
            # if isinstance(c, str):
            c = c.decode('unicode_escape')
            f.write(c + '\n')
    print('create success: %s' % filename)


class LeetCodeCrawler:
    def __init__(self):
        headers = {
            'User-Agent': generate_user_agent(os=('mac', 'linux')),
        }
        self.sess = requests.Session()
        self.sess.headers.update(headers)
        self.timeout = 5

    def crawl_from_url(self, url, **kwargs):
        # name = url.split('problems')[-1].split('/')[0]
        res = self.sess.get(url, timeout=self.timeout)
        root = etree.HTML(res.text)
        question_descrition_list = root.xpath('//div[@class="question-description"]//text()')
        if len(question_descrition_list) == 0:
            return False
        question_descrition = ''.join(question_descrition_list)

        # find config in script
        scripts = [i for i in root.xpath('//script') if not i.attrib and 'pageData' in i.text]
        assert len(scripts) == 1
        pageData = scripts[0].text
        pageDataDict = clear_pagedata(pageData)
        codeDefinition = pageDataDict['codeDefinition']
        code_def = [i['defaultCode'] for i in codeDefinition if i['text'].lower() == kwargs.get('language')]
        code_def = code_def[0] if code_def else ''
        create_leetcode_exercise(pageDataDict['questionTitleSlug'], question_descrition, code_def)

    def crawl(self, **kwargs):
        urls = kwargs.pop('url')
        if not urls:
            # TODO random leetcode
            pass
        for url in urls:
            self.crawl_from_url(url, **kwargs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""www.leetcode.com crawler""")
    parser.add_argument('-u', '--url', type=str, help='url of leetcode problem', nargs='*', default=None)
    parser.add_argument('-l', '--language', type=str, default="python", help='code language')
    parser.add_argument('-d', '--difficulity', type=str, default="medium", help='problem difficulity')
    parser.add_argument('-f', '--findanswer', type=bool, default=False, help='whether find answer')
    args = parser.parse_args()
    lcc = LeetCodeCrawler()
    print(args)
    lcc.crawl(**args.__dict__)
