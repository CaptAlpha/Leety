# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        

        if root1 is None and root2 is None:
            return None

        if root1:
            v1 = root1.val
        else:
            v1 = 0

        if root2:
            v2 = root2.val
        else:
            v2 = 0
        root = TreeNode(v1+v2)

        root.left = self.mergeTrees(root1.left if root1 is not None else None, root2.left if root2 is not None else None)
        
        root.right = self.mergeTrees(root1.right if root1 is not None else None, root2.right if root2 is not None else None)


        return root
        