class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]  # Initialize the stack with the first character
        for i in s[1:]:  # Start iteration from the second character
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
