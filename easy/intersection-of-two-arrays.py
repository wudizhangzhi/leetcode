# coding=utf8
from deco import runningtime

'''
 Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:

    Each element in the result must be unique.
    The result can be in any order.

'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums2:
            return []
        return [i for i in set(nums2) if i in nums1]

    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1)&set(nums2))

if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    sol = Solution()
    print sol.intersection(nums1, nums2)
    print sol.intersection2(nums1, nums2)
