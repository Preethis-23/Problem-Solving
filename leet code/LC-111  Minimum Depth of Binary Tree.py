# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])

        while q:
            root, val = q.popleft()
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return val
            if root.left:
                q.append((root.left, val + 1))
            if root.right:
                q.append((root.right, val + 1))
        