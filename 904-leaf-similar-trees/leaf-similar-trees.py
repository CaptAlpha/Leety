# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # def bfs(root):
        #     l = []
        #     result = []
        #     queue = deque([root])
        #     # if root.left.val is None and root.right.val is None:
        #     #     l.append(root.val)
        #     if not root:
        #         # l.append(root.val)
        #         return []
        #     while(queue):
        #         n = len(queue)
        #         currentLevel = []
        #         for i in range(n):
        #             node = queue.popleft()
        #             print(f'Current Node is {node.val}')
        #             currentLevel.append(node.val)
        #             if node.left:
        #                 queue.append(node.left)
    
        #             if node.right:
        #                 queue.append(node.right)

        #             if not node.right and not node.left:
        #                 l.append(node.val)
            
        #         result.append(currentLevel)
        #     print(l)
        #     return result
        # print(bfs(root1))
        # print(bfs(root2))

        #DFS
        def dfs(root):
            if not root:
                return []
            stack, res = [root], []
            while(stack):
                node = stack.pop()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                if not node.left and not node.right:
                    res.append(node.val)
            return res
        print(dfs(root1))
        print(dfs(root2))
        return dfs(root1) == dfs(root2)
        