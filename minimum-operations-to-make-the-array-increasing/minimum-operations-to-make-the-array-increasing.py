class Solution:
    def minOperations(self, nums: List[int]) -> int:

        ops = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                ops += nums[i] - nums[i+1] + 1
                nums[i+1]+=nums[i] - nums[i+1] + 1
        if len(nums) >= 2:
            if nums[-2] >= nums[-1]:
                ops+= nums[-2]-nums[-1]+1
        return ops



