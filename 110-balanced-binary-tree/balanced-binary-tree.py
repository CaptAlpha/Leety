# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        if (not root.left and not root.right):
            return True
        
        def depth(root):
            if not root:
                return 0
        
            return max(depth(root.left), depth(root.right)) + 1
        
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        
        # Check current node's balance AND recursively check left and right subtrees
        return (abs(left_depth - right_depth) <= 1 and 
                self.isBalanced(root.left) and 
                self.isBalanced(root.right))