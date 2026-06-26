# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def find(tot, path, root):
            nonlocal result
            if root is None:
                return False
            tot += root.val
            path.append(root.val)

            if root.left is None and root.right is None:
                if tot == targetSum:
                    result.append(path[:])

            find(tot, path, root.left)
            find(tot, path, root.right)
            path.pop()
        find(0, [], root)
        return result
        