# coding=utf8
from deco import runningtime
"""
Given a binary search tree with non-negative values, find the 
minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # find all node's val
        result = []
        self.minum = None
        def findallnode(node):
            if result:
                for i in result:
                    tmp = abs(node.val - i)
                    if not self.minum or tmp < self.minum:
                        self.minum = tmp
            result.append(node.val)
            if node.left:
                findallnode(node.left)
            if node.right:
                findallnode(node.right)
        findallnode(root)
        return self.minum

    def getMinimumDifference2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pre, ans = float('-inf'), float('inf')
        stack = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                p = stack.pop()
                print p.val, pre
                ans, pre = min(ans, abs(p.val - pre)), p.val
                curr = p.right
        return ans

if __name__ == '__main__':
    import random
    # Input = [random.randint(0, 100) for i in xrange(10)]
    '''
         3
        / \
      10   100
      / \
    77   33
    '''
    Input = TreeNode(3, TreeNode(10,TreeNode(77), TreeNode(33)), TreeNode(100)) 
    # print Input
    sol = Solution()
    ouput = sol.getMinimumDifference(Input)
    print ouput
    ouput = sol.getMinimumDifference2(Input)
    print ouput
