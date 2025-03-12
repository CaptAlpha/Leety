class Solution:
    def addDigits(self, num: int) -> int:
        def calcSum(n):
            s = 0
            for i in str(n):
                s+=int(i)
            return s
        n = num
        while(len(str(n)) != 1):
            n = calcSum(n)
        return n                