class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        maxAvg = float('inf')*-1
        avg = 0
        s = 0

        if len(nums) < k:
            return sum(nums)/len(nums)

        while(j < len(nums)):
            s += nums[j]
            if (j-i+1) < k:
                j+=1
            elif (j-i+1) == k:
                currAvg = s/k
                maxAvg = max(maxAvg, currAvg)
                s -= nums[i]
                i+=1
                j+=1
        return maxAvg

