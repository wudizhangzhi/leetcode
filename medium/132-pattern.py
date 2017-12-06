#coding=utf8

'''
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import deque
        if len(nums) < 3:
            return False
        s3 = float('-inf')
        stack = []  
        #stack = deque()
        for i in range(len(nums)-1, -1, -1):
            # nums[i] s1 candidate
            print(i, nums[i], stack, s3) 
            if nums[i] < s3:
                return True
            while len(stack)>0 and nums[i] > stack[0]: 
                s3 = stack[0]  
                #s3 = stack.popleft()
                stack.pop()
            stack.append(nums[i])
            print(stack, s3)
            print('-------------------')
        else:
            return False

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        k_stack = [- sys.maxint - 1]
        for l in range(len(nums)-1, -1, -1):
            if nums[l] < k_stack[-1]: return True
            else:
                while k_stack and nums[l] > k_stack[-1]: v = k_stack.pop()
                k_stack.append(nums[l])
                k_stack.append(v)
        return False

if __name__ == '__main__':
    inputs = [-2,1,2,-2,1,2] 
    #inputs = [-1, 3, 2, 2, 3, 0]
    #inputs = [-2,1,1]
    sol = Solution()
    result = sol.find132pattern(inputs)
    print(result)
