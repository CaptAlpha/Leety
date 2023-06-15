class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0
        curr = 0
        for i in s:
            if i == "(":
                stack.append(i)
                curr+=1
            elif i == ")":
                if stack[-1] == "(":
                    stack.pop()
                    curr-=1
            depth = max(depth, curr)
        return depth

