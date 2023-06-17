class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor==-1 and dividend==-2147483648:
            return 2147483647
        return int(dividend/divisor)
