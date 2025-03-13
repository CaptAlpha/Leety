class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c= nums[0]
        for i in nums[1:]:
            c^=i
        return c