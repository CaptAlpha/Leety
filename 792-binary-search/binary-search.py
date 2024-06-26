class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        mid = (low - (low-high)//2)

        while(low<=high):
            if (nums[mid] == target):
                return mid
            elif(nums[mid]>target):
                high = mid-1
            else:
                low = mid+1
            mid = int(low - (low-high)//2)
        return -1         