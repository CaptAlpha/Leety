class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        s = s.split(" ")
        for i in range(len(s)):
            if i == len(s)-1:
                word =s[i]
                res+=word[::-1]
            else:
                word =s[i]
                res+=word[::-1]
                res+=" "

        return res
