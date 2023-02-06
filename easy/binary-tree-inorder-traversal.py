from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        中序遍历： 左自树，根节点，右子树
        """

        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
            if root
            else []
        )


if __name__ == "__main__":
    root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    print(Solution().inorderTraversal(root))
