# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        result = []
        cnt = 0
        while q:
            length = len(q)
            temp = []
            for i in range(length):
                node = q.popleft()
                if node is None:
                    return []
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            cnt += 1
            if cnt % 2 != 0:
                result.append(temp)
            else:
                result.append(temp[::-1])
        return result


        