# coding=utf8
from deco import runningtime


'''
 Given an array nums, write a function to move all 0's to the end of it while
 maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        while (0 in nums):
            nums.remove(0)
            count +=1
        nums.extend([0 for i in xrange(count)])

        return nums

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(cmp=lambda a,b: 0 if b else -1)
        return nums

    def moveZeroes3(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        思路：依次判断，如果不是0，就往前挪
        """
        last0 = 0
        for i in xrange(len(nums)):
            if (nums[i] != 0):
                nums[last0], nums[i] = nums[i], nums[last0]
                last0 += 1

        return nums


if __name__ == '__main__':
    test = [0, 1, 0, 3, 12]
    sol = Solution()
    # print sol.moveZeroes(test)
    # print sol.moveZeroes2(test)
    print sol.moveZeroes3(test)
