class Solution:
    def convert(self, n, k, res=""):
        if n < k:
            res += str(n)
            return res.count('1')
        res += str(n % k)
        n //= k  # Update: Divide n by k, not n %= k
        return self.convert(n, k, res)




    def countBits(self, n: int) -> List[int]:
        return [self.convert(i, 2, "") for i in range(n+1)]
