class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        small = word1 if len(word1) < len(word2) else word2
        large = word1 if len(word1) > len(word2) else word2


        n = len(small)

        for i in range(len(small)):
            ans+=word1[i]+word2[i]
        ans+=large[len(small):]

        return ans
        