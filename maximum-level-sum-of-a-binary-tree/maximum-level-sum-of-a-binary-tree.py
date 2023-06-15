# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.dic= {}
        

        def dfs(root, level):
            level+=1

            if root is None:
                return 

            if level not in self.dic:
                self.dic[level] = [root.val]
            else:
                self.dic[level].append(root.val)

            dfs(root.left, level)
            dfs(root.right, level)

        dfs(root, 0)

        maxSum = float('-inf')

        maxLevel = -1

        for i, j in self.dic.items():
            
            if maxSum < sum(j):
                print(i, j, sum(j))
                maxSum = sum(j)
                maxLevel = i
        


        return maxLevel

        
            