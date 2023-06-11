# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def giveArray(self, root, li):
        if root is None:
            return
        li.append(root.val)
        self.giveArray(root.left, li)
        self.giveArray(root.right, li)

        return li

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return TreeNode()
        li = []
        li = self.giveArray(root, li)
        li.sort()

        new_root = TreeNode(li[0])
        current = new_root

        for i in range(1, len(li)):
            current.right = TreeNode(li[i])
            current = current.right

        


        return new_root


        