class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cpy = nums[:]
        cpy.sort()
        ans = []
        for i in nums:
            ans.append(cpy.index(i))
        return ans