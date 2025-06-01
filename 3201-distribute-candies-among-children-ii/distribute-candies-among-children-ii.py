from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def count_solutions(x):
            # Counts non-negative integer solutions to a + b + c = x
            if x < 0:
                return 0
            return comb(x + 2, 2)

        total = count_solutions(n)

        # Subtract cases where a > limit
        total -= 3 * count_solutions(n - limit - 1)

        # Add back cases where two variables > limit
        total += 3 * count_solutions(n - 2 * (limit + 1))

        # Subtract cases where all three variables > limit
        total -= count_solutions(n - 3 * (limit + 1))

        return total