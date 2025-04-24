from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_elements = len(set(nums))
        count = 0
        n = len(nums)
        
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == distinct_elements:
                    count += 1
        
        return count