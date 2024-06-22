class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new = []
        for i in range(len(nums)):
            new.append(0)
            
        for i in range(len(nums)):
            new[i] = nums[nums[i]]
        
        return new