class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        firstPos = -1
        lastPos = -1

        # we do binary search twice
        start = 0
        end = len(nums) - 1
         # first to find the smallest guy
        while(start <= end):
            mid = (start+end) // 2

            if target == nums[mid]:
                firstPos = mid
                end = mid - 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # Reseting my folks
        start = 0
        end = len(nums) - 1
        # we then find the last occurence
        while(start <= end):
            mid = (start+end) // 2

            if target == nums[mid]:
                lastPos = mid
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return [firstPos, lastPos]