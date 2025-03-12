class Solution:
    def countEven(self, num: int) -> int:

        def calcSum(n):
            s = 0
            for i in str(n):
                s += int(i)
            return s
        
        c = 0

        for i in range(num+1):
            if (calcSum(i) & 1 == 0):
                c+=1
        return c-1
        