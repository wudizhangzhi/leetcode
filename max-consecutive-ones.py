# coding=utf8
from deco import runningtime

'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000

'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        for num in nums:
            if num == 1:
                a += 1
                b = max(a, b)
            else:
                a = 0
        return b




if __name__ == '__main__':
    nums = [1,0,1,1,0,1]
    sol = Solution()
    res = sol.findMaxConsecutiveOnes(nums)
    print res