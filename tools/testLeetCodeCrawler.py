# coding=utf8
from nose.tools import assert_equal, assert_true, assert_in
from nose.tools import with_setup

import unittest

from LeetCodeCrawler import LeetCodeCrawlerObject, LEVEL_DICT


def repeat(times=10):
    def deco(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return deco


class TestLeetCodeCrawler(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.lcc = LeetCodeCrawlerObject()
        super(TestLeetCodeCrawler, self).__init__(*args, **kwargs)

    def setUp(self):
        print("============test math module setup==============\n")
        self.problems = self.lcc.fetch_all_problem()
        assert_true(len(self.problems) > 0)
        assert_true(len([p for p in self.problems if p['difficulty']['level'] == 1]) > 0)
        assert_true(len([p for p in self.problems if p['difficulty']['level'] == 2]) > 0)
        assert_true(len([p for p in self.problems if p['difficulty']['level'] == 3]) > 0)

    def tearDown(self):
        print("============test math module teardown==============\n")

    @classmethod
    def setUpClass(cls):
        print("============test math class setup==============\n")

    @classmethod
    def tearDownClass(cls):
        print("============test math class teardown==============\n")

    # def test_fetchallproblems(self):  # 测试获取全部问题
    #     self.problems = self.lcc.fetch_all_problem()
    #     assert_true(len(self.problems) > 0)
    #     assert_true(len([p for p in self.problems if p['difficulty']['level'] == 1]) > 0)
    #     assert_true(len([p for p in self.problems if p['difficulty']['level'] == 2]) > 0)
    #     assert_true(len([p for p in self.problems if p['difficulty']['level'] == 3]) > 0)

    # @unittest.skip("I don't want to run this case.")
    # @with_setup(test_fetchallproblems)
    # @repeat(times=10)
    def test_choseone_with_noparams(self):  # 测试选择一个，没有参数
        problem = self.lcc.choice_one(self.problems)
        assert_true(problem)
        assert_in('stat', problem)
        assert_in('difficulty', problem)
        assert_in('question__title_slug', problem['stat'])
        assert_in('level', problem['difficulty'])

    # @repeat(times=10)
    def test_choseone_with_params(self):
        languages = ['python']
        difficulties = LEVEL_DICT.values()
        for language in languages:
            for difficulity in difficulties:
                kwargs = {'language': language, 'difficulty': difficulity}

                problem = self.lcc.choice_one(self.problems, **kwargs)
                assert_true(problem)
                assert_in('stat', problem)
                assert_in('difficulty', problem)
                assert_in('question__title_slug', problem['stat'])
                assert_in('level', problem['difficulty'])
                assert_equal(difficulity, LEVEL_DICT.get(problem['difficulty']['level'], ''))


if __name__ == '__main__':
    unittest.main()
