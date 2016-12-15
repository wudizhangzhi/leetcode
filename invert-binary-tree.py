# coding=utf8
from deco import runningtime
'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root

    def invert(self, root):
        next_level = []
        if not isinstance(root, list):
            root = [root]
        for i in root:
            if i:
                i.right, i.left = i.left, i.right
                if isinstance(i.left, TreeNode):
                    next_level.append(i.left)
                if isinstance(i.right, TreeNode):
                    next_level.append(i.right)
        if next_level:
            self.invert(next_level)


    def invertTree2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.right, root.left = self.invertTree2(root.left), self.invertTree2(root.right)
            return root

    def printTree(self, root):
        if not isinstance(root, list):
            root = [root]
        this_level = []
        next_level = []
        for i in root:
            if isinstance(i, int):
                this_level.append(i)
            else:
                this_level.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
        if this_level:
            print this_level
        if next_level:
            self.printTree(next_level)




from collections import namedtuple
import time
'''
           1
         /   \
       /       \
      /         \
     2           3
    / \         / \
   /   \       /   \
   4    5     6     7

'''
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

# Node = namedtuple('node', ['val', 'left','right'])
# tree = Node(1,
#             Node(2,
#                  4,
#                  5),
#             Node(3,
#                  6,
#                     7),
#                  )
tree = TreeNode(1,
            TreeNode(2,
                 4,
                 5),
            TreeNode(3,
                 6,
                    None),
                 )
if __name__ == '__main__':
    sol = Solution()
    sol.printTree(tree)
    start = time.time()
    root = sol.invertTree(tree)
    print time.time()-start
    sol.printTree(root)

    start = time.time()
    root = sol.invertTree2(tree)
    print time.time()-start
    sol.printTree(root)
