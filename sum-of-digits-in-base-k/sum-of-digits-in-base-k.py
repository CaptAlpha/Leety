class Solution:
    def convert(self, n, k, res=""):
        if n < k:
            res += str(n)
            return res
        res += str(n % k)
        n //= k  # Update: Divide n by k, not n %= k
        return self.convert(n, k, res)
        
    def sumBase(self, n: int, k: int) -> int:
        num = self.convert(n, k)
        counter = 0
        for i in num:
            counter += int(i)
        return counter
