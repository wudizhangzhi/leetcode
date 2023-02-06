from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.val}"


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen = []

        def dfs(node: Optional[TreeNode]):
            if node.left:
                dfs(node.left)
            seen.append(node.val)
            if len(seen) >= k:
                return
            if node.right:
                dfs(node.right)

        dfs(root)
        return seen[k - 1]


if __name__ == "__main__":
    root = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
    print(Solution().kthSmallest(root, 2))
