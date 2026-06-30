# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def dfs(root):
            nonlocal ans
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(0, left)
            right = max(0, right)
            ans = max(ans,root.val + left + right)

            return root.val + max(left, right)
        dfs(root)
        return ans
#exactly like lc - 543 diameter of binary tree