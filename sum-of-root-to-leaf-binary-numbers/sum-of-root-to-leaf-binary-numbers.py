# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convert(self, n):
        res = 0
        s = str(n)
        s = s[::-1]
        place = 0
        for i in s:
            res+=(2**(place)*int(i))
            place+=1
        print(res)
        return res

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return None
        results = []
        self.helper(root, 0, results)
        print(results)
        res = 0
        for i in results:
            res+=self.convert(i)

        return res
    
    def helper(self, node, pathSum, result):
        if node is None:
            return 
        pathSum = pathSum*10 + node.val
        if node.right is None and node.left is None:
            result.append(pathSum)
        self.helper(node.left, pathSum, result)
        self.helper(node.right, pathSum, result)
