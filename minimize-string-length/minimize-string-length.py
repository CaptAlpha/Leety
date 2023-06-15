class Solution:
    def minimizedStringLength(self, s: str) -> int:
        stack = []
        stack = list(s)
        return len(list(set(stack)))
