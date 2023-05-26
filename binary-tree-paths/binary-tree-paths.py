# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode], li = []) -> List[str]:
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]  # Initialize stack with root and its path

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:  # Leaf node
                paths.append(path)
            
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
            
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))

        return paths