class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Finding the ceiling 

        start = 0
        end = len(nums) - 1
        res = -1
        while(start <= end):
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                res = mid
                start = mid+1
            else:
                end = mid-1
        return res+1
