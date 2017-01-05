# coding=utf8
from deco import runningtime

'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements
 appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
class Solution(object):
    @runningtime
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # if not nums:
        #     return []
        return list(set([i for i in xrange(1, len(nums) + 1)]).difference(set(nums)))

    def findDisappearedNumbers2(self, nums):
        # 思路：讲nums中的数字转换为负数，
        # 然后没有在[1, n]列表中出现的数字的位置就是正数
        # 返回这些正数的位置+1就行
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        return nums

if __name__ == '__main__':
    Input = [1, 2, 2, 2, 3, 4, 7, 8]

    sol = Solution()
    # Output = sol.findDisappearedNumbers(Input)
    Output = sol.findDisappearedNumbers2(Input)
    print Output
