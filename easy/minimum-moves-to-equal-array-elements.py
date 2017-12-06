# coding=utf8
from deco import runningtime

'''
Given a non-empty integer array of size n, find the minimum number of moves
 required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
需要的最少步骤，
每一步使n-1个元素 +1
'''
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        排序后
        nums = [a0,a1,a2,....an]
        序号       数值
        0         a1-a0
        1         a2-a1+a1-a0=a2-a0
        2         a3-a0
        .         .
        .         .
        .         .
        n-1       an-a0
        -------------------
        和 =      a1+a2+...an - a0*(n-1)=sum(nums) - a0*n
        """
        return sum(nums) - min(nums)*len(nums)



if __name__ == '__main__':
    Input = [1,2,3]

    sol = Solution()
    # Output = sol.findDisappearedNumbers(Input)
    Output = sol.minMoves(Input)
    print 'Output:%s' % Output
