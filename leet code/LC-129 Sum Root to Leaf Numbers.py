# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        tot = 0
        def find(root, string):
            nonlocal tot
            if not root:
                return
            string += str(root.val)
            if not root.left and not root.right:
                tot += int(string)
                return
            find(root.left, string)
            find(root.right, string)
        find(root, "")
        return tot
        