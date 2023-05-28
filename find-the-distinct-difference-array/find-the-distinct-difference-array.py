class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        li = []
        n = len(nums)
        p = []
        for i in range(n):
            li.append(len(set(nums[:i+1]))-len(set(nums[i+1:])))
        
        return li