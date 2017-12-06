# coding=utf8
from deco import runningtime
'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution(object):
    @runningtime
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # return next(([i+1, numbers[i+1:].index(target-numbers[i])+i+2] for i in xrange(len(numbers)) if numbers[i+1:].count(target-numbers[i])))
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

    @runningtime
    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            temp = numbers[l] + numbers[r]
            if temp == target:
                return [l+1, r+1]
            elif temp > target:
                r -= 1
            else:
                l += 1




if __name__ == '__main__':
    # numbers = [2, 7, 11, 15]
    numbers = [i for i in xrange(10000)]
    target = 19997
    sol = Solution()
    result = sol.twoSum(numbers, target)
    print result
    result = sol.twoSum2(numbers, target)
    print result
