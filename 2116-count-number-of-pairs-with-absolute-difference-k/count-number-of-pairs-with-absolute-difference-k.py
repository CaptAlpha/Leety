class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        x = (list(combinations(nums, 2)))
        c = 0
        for i in x:
            if abs(i[0]-i[1]) == k:
                c+=1
        return c