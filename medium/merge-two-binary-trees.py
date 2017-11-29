# -*- coding:utf8 -*-

"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2



def print_node(node):
    print(node.val)
    def _print_node(nodelist):
        next_level = []
        for node in nodelist:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if next_level:
            print([i.val for i in next_level])
            _print_node(next_level)
        else:
            return
    _print_node([node])


'''
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
'''
if __name__ == '__main__':
    t1 = TreeNode(1, left=TreeNode(3,left=TreeNode(5)), right=TreeNode(2))
    t2 = TreeNode(2, left=TreeNode(1, right=TreeNode(4)), right=TreeNode(3, right=TreeNode(7)))
    sol = Solution()
    result = sol.mergeTrees(t1, t2)
    print_node(result)
