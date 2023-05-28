class Solution:
    def longestPalindrome(self, s: str) -> str:


        if s == s[::-1]:
            return s
        
        res = ""
        for i in range(len(s)-1):
            for j in range(i+1, len(s)+1):
                word = s[i:j]
                if word == word[::-1]:
                    if (len(word)>len(res)):
                        res = word

        return res