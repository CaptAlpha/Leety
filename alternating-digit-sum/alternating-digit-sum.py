class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        s = list(str(n))

        for i in range(len(s)):
            if i%2==0:
                res+=(int(s[i]))
            else:
                res+=(-1*(int(s[i])))
        return res