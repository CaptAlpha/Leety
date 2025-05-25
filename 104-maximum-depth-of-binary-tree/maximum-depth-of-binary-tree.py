# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            level = 0
            queue = deque([root])

            if not root:
                return 0

            while(queue):

                levelSize = len(queue)
                

                for i in range(levelSize):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                level+=1
            
            return level
        
        return bfs(root)