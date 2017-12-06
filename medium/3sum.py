#coding=utf8

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        for i in xrange(length):
            for j in xrange(i+1, length):
                for x in xrange(j+1, length):
                    a1 = nums[i]
                    a2 = nums[j]
                    a3 = nums[x]
                    if a1 + a2 + a3 == 0:
                        one = sorted([a1, a2, a3])
                        if one not in result:        
                            result.append(one)
        return result


if __name__ == '__main__':
    s = [-1, 0, 1, 2, -1, -4] 
    sol = Solution()
    output = sol.threeSum(s)
    print(output)
