class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        prefixMin = nums[0] # this variable will store the minimum uptill i index (or current index)

        # by default the prefixMin for nums[1]  will be nums[0]
        for i in range(1, len(nums)): # this will go from 1 to last element

            if nums[i] > prefixMin: # if current element is greater than prefixMin(lowest element found so far)
            # update the maxDiff by comparing with current value of maxDiff and current num - prefixMin
                maxDiff = max(maxDiff, nums[i] - prefixMin)

            else: # if the current element is smaller than the prefix min itself
            # update the prefixMin with current element (else case)
                prefixMin = nums[i]

        return maxDiff