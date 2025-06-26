class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        temp = 0
        n = len(s)
        current = 0

        for i in range(n-1,-1,-1):
            if s[i] == "0":
                temp += 1
            if s[i] == "1":
                current += 2**(n-i-1)
                if current <= k:
                    temp +=1
        return(temp)