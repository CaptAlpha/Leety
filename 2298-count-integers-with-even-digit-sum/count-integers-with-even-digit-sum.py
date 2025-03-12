class Solution:
    def countEven(self, num: int) -> int:

        def calcSum(n):
            s = 0
            for i in str(n):
                s += int(i)
            return s

        if calcSum(num) & 1 == 1:
            #odd
            return (num-1)//2
        else:
            return num//2
        