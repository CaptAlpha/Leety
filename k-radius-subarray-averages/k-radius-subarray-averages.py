from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        li = []
        n = len(nums)
        window_sum = sum(nums[:2*k+1])
        
        for i in range(len(nums)):
            if i >= k and n-i>k:
                li.append(window_sum // (2 * k + 1))
                if i < n - k - 1:
                    window_sum += nums[i + k + 1] - nums[i - k]
            else:
                li.append(-1)
        
        return li
