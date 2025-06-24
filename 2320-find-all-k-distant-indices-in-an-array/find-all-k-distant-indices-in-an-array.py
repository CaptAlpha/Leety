from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = [i for i in range(len(nums)) if nums[i] == key]
        res = set()

        for j in key_indices:
            # Add all indices within distance k of j
            for i in range(max(0, j - k), min(len(nums), j + k + 1)):
                res.add(i)

        return sorted(res)


        