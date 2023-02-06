"""
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        import queue

        heap = queue.Queue()

        heap.put((p, q))

        def check(n1, n2):
            if n1 is None and n2 is None:
                return True

            elif n1 is None or n2 is None:
                return False

            elif n1.val != n2.val:
                return False
            else:
                return True

        while not (heap.empty()):
            n1, n2 = heap.get()
            res = check(n1, n2)
            if not res:
                return False
            else:
                if n1 and n2:
                    heap.put((n1.left, n2.left))
                    heap.put((n1.right, n2.right))
        return True
