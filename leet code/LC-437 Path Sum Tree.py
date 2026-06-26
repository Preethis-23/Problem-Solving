# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        def find(tot, root):
            nonlocal cnt
            if not root:
                return
            tot += root.val

            if tot == targetSum:
                cnt += 1
            find(tot, root.left)
            find(tot, root.right)

        
        def send(root):
            if not root:
                return
            find(0, root)
            send(root.left)
            send(root.right)
        send(root)
        return cnt