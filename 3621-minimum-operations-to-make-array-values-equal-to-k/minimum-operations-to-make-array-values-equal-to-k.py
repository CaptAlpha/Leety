class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        if nums[-1] < k: 
            return -1
        elif nums[-1] == k: 
            return len(set(nums)) -1
        elif nums[-1] > k: 
            return len(set(nums))