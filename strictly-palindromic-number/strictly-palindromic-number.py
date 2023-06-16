class Solution:
    def convert(self, n, k, res=""):
        if n < k:
            res += str(n)
            return res

        res += str(n % k)
        n //= k
        return self.convert(n, k, res)

    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n + 1):
            word = self.convert(n, i)
            if word != word[::-1]:
                return False
        return True