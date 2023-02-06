# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = [(root, 1)]
        while q:
            node, level = q.pop(0)
            if not node:
                break
            if level > len(ans):
                ans.append(node.val)
            if node.right:
                q.append((node.right, level + 1))
            if node.left:
                q.append((node.left, level + 1))

        return ans
