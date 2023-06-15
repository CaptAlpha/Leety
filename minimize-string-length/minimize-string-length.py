class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(list(set(list(s))))
