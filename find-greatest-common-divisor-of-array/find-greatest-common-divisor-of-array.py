class Solution:
    def gcd(self, a, b):
        if b==0:
            return a
        return self.gcd(b, a%b)
    def findGCD(self, nums: List[int]) -> int:
        mi = min(nums)
        ma = max(nums)
        return self.gcd(mi, ma)
