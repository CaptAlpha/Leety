class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        maxidx, minidx = -1, -1
        cur_max_idx, cur_min_idx = -1, -1
        result = 0
        for i in range(len(nums)):
            if nums[i] == maxK:
                maxidx = i
            if nums[i] == minK:
                minidx = i
            if nums[i] > maxK:
                cur_max_idx = i
            elif nums[i] < minK:
                cur_min_idx = i
            else:
                idxr = min(maxidx, minidx)
                idxl = max(cur_max_idx, cur_min_idx)
                result += max(idxr - idxl, 0)

        return result