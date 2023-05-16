class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        a, b = nums[-2], nums[-1]
        c, d = nums[0], nums[1]
        return (a*b)-(c*d)