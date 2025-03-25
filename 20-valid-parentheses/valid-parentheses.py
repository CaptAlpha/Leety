class Solution:
    def isValid(self, s: str) -> bool:
        h = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in h.values():  # If it's an opening bracket
                stack.append(char)
            else:  # If it's a closing bracket
                if not stack or stack.pop() != h[char]:
                    return False
        return len(stack) == 0
        return True if len(stack) == 0 else False