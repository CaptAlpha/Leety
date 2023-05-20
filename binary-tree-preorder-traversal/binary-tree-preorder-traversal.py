# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        def pre(root, li):
            if root is None:
                return 
            li.append(root.val)
            pre(root.left, li)
            pre(root.right, li)

        pre(root, li)

        return li
        