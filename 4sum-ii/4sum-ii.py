class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        sum_dict = {}
        
        for i in nums1:
            for j in nums2:
                sum_dict[i + j] = sum_dict.get(i + j, 0) + 1
        
        for k in nums3:
            for l in nums4:
                count += sum_dict.get(-(k + l), 0)
        
        return count