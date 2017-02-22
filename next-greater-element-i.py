# coding=utf8
from deco import runningtime
'''
 You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

'''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # return map(lambda x:nums[nums.index(x) +1] if nums.index(x)<(len(nums)-1) else -1, findNums)
        def findgrader(x):
            index = nums.index(x)
            if nums.index(x) >= (len(nums)-1):
                return -1
            for i in xrange(index, len(nums)):
                if nums[i] > x:
                    return nums[i]
            else:
                return -1

        return map(findgrader, findNums)


    def nextGreaterElement2(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        return [next((x for x in nums[nums.index(f):] if x > f) ,-1) for f in findNums]


if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    sol = Solution()
    output = sol.nextGreaterElement(nums1, nums2)
    print output
    output = sol.nextGreaterElement2(nums1, nums2)
    print output
