class Solution:
    def maxSum(self, nums: List[int]) -> int:
        arr = set()
        for i in nums:
            if i >=0:
                arr.add(i)
        
        if len(arr) == 0:
            return max(nums)
        
        return sum(arr)