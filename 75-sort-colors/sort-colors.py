class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = b = 0
        for i in range(len(nums)):
            if nums[i] == 0: a+=1
            if nums[i] == 1: b+=1
        
        for i in range(len(nums)):
            if i < a: nums[i] = 0
            elif i >= a and i < a+b: nums[i] = 1
            else: nums[i] = 2
        

            

        