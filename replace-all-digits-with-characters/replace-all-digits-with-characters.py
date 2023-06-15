class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""

        

        for i in range(0, len(s)-1, 2):
            res+=s[i]
            res+=chr(ord(s[i])+int(s[i+1]))

        if len(s)%2 == 1:
            last = s[-1]
            return res+last

        return res