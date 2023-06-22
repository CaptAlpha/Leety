class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n                 
# Here reminder is taken because if we had 10 rotation but our numsay is of size 9 then only 1 rotation is effective to produce ans.

        nums[n - k:] = nums[n - k:][::-1] # Reverse n - k to end of the numsay 
        nums[:n - k] = nums[:n - k][::-1] # Reverse 0 to n - k  
        nums[:] = nums[::-1]              # Reverse whole array
