class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, -1
        # for i in nums:
        #     if i==target:
        #         left = i
        #         break
        # for i in nums[::-1]:
        #     if i==target:
        #         right = 
        #         break

        # return [left, right]

        for i in range(len(nums)):
            if nums[i] == target:
                left = i
                break
        nums = nums[::-1]
        for i in range(len(nums)):
            if nums[i] == target:
                right = len(nums) - i - 1
                break
        return [left, right]

        



        
