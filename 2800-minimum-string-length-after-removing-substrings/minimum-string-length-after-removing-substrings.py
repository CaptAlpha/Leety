class Solution:
    def minLength(self, s: str) -> int:
        stack = [s[0]]

        for i in s[1:]:
            if stack and (stack[-1] + i == 'AB' or stack[-1] + i == 'CD'):
                stack.pop()
            else:
                stack.append(i)
        print(stack)
        return len(stack)