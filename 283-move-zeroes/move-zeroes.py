class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[c] = nums[i]
                c+=1
            i+=1
        for i in range(c, len(nums)):
            nums[i] = 0