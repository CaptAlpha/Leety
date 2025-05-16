class Solution:
    def is_one_char_diff(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diff = sum(c1 != c2 for c1, c2 in zip(s1, s2))
        return diff == 1

    def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if (self.is_one_char_diff(words[i], words[j]) and
                    groups[i] != groups[j] and
                    dp[j] + 1 > dp[i]):
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i

        ans = []
        i = max_index
        while i != -1:
            ans.append(words[i])
            i = prev[i]

        return ans[::-1]