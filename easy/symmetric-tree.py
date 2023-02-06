from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        # return f"""
        # {self.val}
        # /\\
        # {self.left} {self.right}
        # """
        return f"{self.val}"


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(left, right) -> bool:
            if (left and right is None) or (left is None and right):
                return False
            if left is None and right is None:
                return True
            if left.val != right.val:
                return False
            return isSym(left.left, right.right) and isSym(left.right, right.left)

        if not root:
            return True
        return isSym(root.left, root.right)


if __name__ == "__main__":
    tree = TreeNode(
        1,
        left=TreeNode(2, right=TreeNode(3)),
        right=TreeNode(2, right=TreeNode(3)),
    )
    print(Solution().isSymmetric(tree))
