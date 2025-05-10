class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_sum, zeros1_count = self.count_and_sum(nums1)
        nums2_sum, zeros2_count = self.count_and_sum(nums2)

        if(zeros1_count == 0 and nums1_sum < nums2_sum) or (zeros2_count==0 and nums2_sum < nums1_sum):
            return -1
        return max(nums1_sum, nums2_sum)
    
    def count_and_sum(self, nums):
        nums_sum = 0
        zeros_count = 0
        for num in nums:
            if num == 0:
                nums_sum += 1
                zeros_count += 1
            else:
                nums_sum += num
        return nums_sum, zeros_count