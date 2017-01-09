# coding=utf8
from deco import runningtime

'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    count = 0
    # def sumOfLeftLeaves(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not isinstance(root, list):
    #         root = [root]
    #     nextlevel = []
    #     for node in root:
    #         if not node:
    #             continue
    #         if node.left:
    #             if isinstance(node.left, int):
    #                 self.count += node.left
    #             elif isinstance(node.left, TreeNode):
    #                 self.count += node.val
    #         if isinstance(node.left, TreeNode):
    #             nextlevel.append(node.left)
    #         if isinstance(node.right, TreeNode):
    #             nextlevel.append(node.right)
    #
    #     if nextlevel:
    #         return self.sumOfLeftLeaves(nextlevel)
    #     else:
    #         return self.count

    def sumOfLeftLeaves2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right: #节点的左边是数字
            return root.left.val + self.sumOfLeftLeaves2(root.right)
        return self.sumOfLeftLeaves2(root.left) + self.sumOfLeftLeaves2(root.right)




if __name__ == '__main__':
    testdata = TreeNode(3, left=TreeNode(9), right=TreeNode(20, TreeNode(15), TreeNode(7)))
    sol = Solution()
    output = sol.sumOfLeftLeaves(testdata)
    print output
    output = sol.sumOfLeftLeaves2(testdata)
    print output
