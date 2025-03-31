from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0  # Edge case
        
        pair_sum = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        pair_sum.sort()

        min_sum = sum(pair_sum[:k - 1])
        max_sum = sum(pair_sum[-(k - 1):])

        return max_sum - min_sum