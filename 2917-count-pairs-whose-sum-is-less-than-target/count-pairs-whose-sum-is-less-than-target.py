class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Sort the array to use two-pointer technique
        nums.sort()
        count = 0
        left = 0
        right = len(nums) - 1
        
        # Use two pointers to find pairs with sum less than target
        while left < right:
            if nums[left] + nums[right] < target:
                # If nums[left] + nums[right] < target, all pairs (left, left+1), (left, left+2), ..., (left, right) are valid
                count += (right - left)
                left += 1
            else:
                right -= 1
                
        return count