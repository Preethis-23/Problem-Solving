# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ind = 0
        inorder_index = {val:i for i, val in enumerate(inorder)}
        def build(left,right):
            nonlocal ind
            if left>right:
                return None
            
            root_val = preorder[ind]
            ind+=1
            new_node = TreeNode(root_val)
            mid = inorder_index[root_val]

            new_node.left = build(left, mid-1)
            new_node.right = build(mid+1, right)

            return new_node
        return build(0, len(inorder)-1)
        
                


        
        