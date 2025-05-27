class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        for i in range(1+n):
            if i%m:
                res+=i
            else:
                res-=i
        return res
                