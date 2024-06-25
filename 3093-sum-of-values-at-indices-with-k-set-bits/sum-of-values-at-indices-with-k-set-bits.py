class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # dic = {}
        s = 0
        for i in range(len(nums)):
            if k == bin(i)[2:].count("1"):
                s+=nums[i]
        return s
        