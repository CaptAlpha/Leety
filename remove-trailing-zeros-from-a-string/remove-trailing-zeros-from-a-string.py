class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        res = ""
        s = list(num)

        while(s[-1] == '0'):
            s.pop()

        for i in s: res+=i
        return res
