#coding=utf8
import sys
sys.path.append('..')
from tools.kuaipai import runningtime
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution(object):
    @runningtime
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) == 1:
                return i
        return -1


class Solution2(object):
    @runningtime
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y: x^y, nums)


class Solution3(object):
    @runningtime
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import operator
        return reduce(operator.xor, nums)



if __name__ == '__main__':
    data = [i for i in xrange(100)]*2 + [333]
    sol = Solution()
    print sol.singleNumber(data)
    sol2 = Solution2()
    print sol2.singleNumber(data)
    sol3 = Solution3()
    print sol3.singleNumber(data)
