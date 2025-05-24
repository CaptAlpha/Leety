from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def bfs(node):
            if not node:
                return []
            result = []
            queue = deque([node])
            while queue:
                level_size = len(queue)
                current_level = []
                for _ in range(level_size):
                    node = queue.popleft()
                    if node:
                        current_level.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        current_level.append(None)
                result.append(current_level)
            return result
        
        left_bfs = bfs(root.left)
        right_bfs = bfs(root.right)
        
        if len(left_bfs) != len(right_bfs):
            return False
        
        for left_level, right_level in zip(left_bfs, right_bfs):
            if left_level != right_level[::-1]:
                return False
        return True