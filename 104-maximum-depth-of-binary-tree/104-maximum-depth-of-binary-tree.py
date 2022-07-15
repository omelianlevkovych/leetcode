# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root) -> int:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 0
            return 1 + max(dfs(root.left), dfs(root.right))
        
        if root is None:
            return 0
        return 1 + dfs(root)