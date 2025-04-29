class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        indices = [i for i, num in enumerate(nums) if num == max_num]
        n = len(nums)
        result = 0
        m = len(indices)
        
        for i in range(m - k + 1):
            left = indices[i] - (indices[i-1] if i > 0 else -1)
            right = n - indices[i + k - 1]
            result += left * right
        
        return result