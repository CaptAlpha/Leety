class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0] / k
        
        max_sum = current_sum = sum(nums[:k])
        max_avg = max_sum / k
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
            max_avg = max_sum / k
        
        return max_avg