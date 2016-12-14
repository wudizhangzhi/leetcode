# coding=utf8
import sys
sys.path.append('..')
from tools.kuaipai import runningtime
'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
 node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    错误，这里求的是最大值的深度
    '''
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.LEVEL = 0
        self.MAX = 0
        self.travel_tree_level_by_level(root)
        return self.LEVEL


    def travel_tree_level_by_level(self, node, level=0):
        next_level = []
        if not isinstance(node, list):
            node = [node]
        for n in node:
            if n.val > self.MAX:
                self.MAX = n.val
                self.LEVEL = level
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        print level, self.LEVEL, self.MAX, len(next_level)
        if next_level:
            self.travel_tree_level_by_level(next_level, level=level+1)
        else:
            return self.LEVEL


class Solution2(object):
    '''
    迭代的思想：假设最后一个，所有的都是None,则返回的是0，再往上一层，不是None，所以返回值是1+0，
    以此类推，每往上一层都+1
    '''
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0


class Solution3(object):
    '''
    减少一个map
    '''
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0


class Solution4(object):
    '''
    听说这个方法快
    '''
    def maxDepth(self, roo]t):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.result = float('-inf') #负无穷
        self.helper(root, 1)
        return self.result


    def helper(self, root, depth):
        if not root.left and not root.right:
            self.result = max(self.result, depth)
        if root.left:
            self.helper(root.left, depth+1)
        if root.right:
            self.helper(root.right, depth+1)



from collections import namedtuple
import time
'''
           1
         /   \
        /     \
       /       \
      /         \
     2           3
    / \         / \
   /   \       /   \
   4    5     6     N
  / \  / \   / \
 7  N N   N 8   9
/ \        / \  / \
N  N      N   N N N
'''

Node = namedtuple('node', ['val', 'left','right'])
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))

if __name__ == '__main__':
    sol = Solution()
    start = time.time()
    print sol.maxDepth(tree)
    print 'running:%s' % (time.time()-start)

    sol2 = Solution2()
    start = time.time()
    print sol2.maxDepth(tree)
    print 'running:%s' % (time.time()-start)

    sol3 = Solution3()
    start = time.time()
    print sol3.maxDepth(tree)
    print 'running:%s' % (time.time()-start)

    sol4 = Solution4()
    start = time.time()
    print sol4.maxDepth(tree)
    print 'running:%s' % (time.time()-start)
