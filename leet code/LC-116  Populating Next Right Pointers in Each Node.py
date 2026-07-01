"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        q = deque([root])

        while q:
            length = len(q)

            for i in range(length):
                node = q.popleft()
                if i + 1 < length:
                    node.next = q[0]
                else:
                    node.next = None
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
                