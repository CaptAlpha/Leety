import math
from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Edge case: If total candies are less than k, return 0
        if sum(candies) < k:
            return 0
        
        # Helper function to check if it's possible to distribute candies with `c` candies per child
        def check(arr, c, k):
            total = 0
            for pile in arr:
                piles_from_pile = pile // c
                total += piles_from_pile
                if total >= k:
                    return True
            return False

        # Binary search to find the maximum number of candies per child
        start = 1
        end = max(candies)

        while start <= end:
            mid = (start + end) // 2
            if check(candies, mid, k):
                start = mid + 1
            else:
                end = mid - 1
        return end