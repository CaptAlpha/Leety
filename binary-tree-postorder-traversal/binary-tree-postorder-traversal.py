# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.l = []
        def post(root):
            if root is None:
                return 
            post(root.left)
            post(root.right)
            self.l.append(root.val)
            return self.l
        return post(root)
            


        