# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        s = []
        def traverse(root):
            if not root:
                return 0
            
            # Calculate the sum of the current subtree
            curr = root.val + traverse(root.left) + traverse(root.right)
            
            # Append the sum to the list
            s.append(curr)
            
            return curr
        
        # Start the traversal
        traverse(root)
        h = Counter(s)
        print(h)
        m = max(list(h.values()))
        print(m)
        ans = []
        for i in s:
            if h[i] == m:
                ans.append(i)
        return list(set(ans))

        

            