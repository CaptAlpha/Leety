class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1, m2 = 0, 0
        nums.sort()
        nums = nums[::-1]
        m1, m2 = nums[0], nums[1]

        return (m1-1)*(m2-1)
