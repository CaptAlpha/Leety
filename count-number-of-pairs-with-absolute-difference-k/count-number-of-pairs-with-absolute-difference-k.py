class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j])==k:
                    counter+=1

        return counter
        