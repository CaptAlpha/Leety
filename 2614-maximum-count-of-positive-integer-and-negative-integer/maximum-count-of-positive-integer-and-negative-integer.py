class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pc, nc = 0, 0
        for i in nums:
            if i > 0: pc += 1
            elif i < 0: nc += 1
        return max(pc, nc)

        