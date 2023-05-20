# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root):
        if root is None:
            return 0
        lh = self.depth(root.left)
        rh = self.depth(root.right)

        return 1+max(lh, rh)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        lh = self.depth(root.left)
        rh = self.depth(root.right)

        if abs(lh-rh)>1:
            return False

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        return left and right
