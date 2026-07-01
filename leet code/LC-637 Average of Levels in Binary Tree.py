# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def level(root):
            q = deque([root])
            result = []

            while q:
                temp = 0
                size = len(q)

                for _ in range(size):
                    root = q.popleft()
                    temp += root.val

                    if root.left:
                        q.append(root.left)
                    if root.right:
                        q.append(root.right)

                result.append(temp / size)
            return result
        return level(root)
