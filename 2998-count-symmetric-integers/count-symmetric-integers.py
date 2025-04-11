class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        def digit_sum(s):
            return sum(int(d) for d in s)
        
        def is_symmetric(n):
            s = str(n)
            length = len(s)
            if length % 2 != 0:
                return False
            half = length // 2
            left = s[:half]
            right = s[half:]
            return digit_sum(left) == digit_sum(right)
        
        for i in range(low, high + 1):
            if is_symmetric(i):
                count += 1
        return count