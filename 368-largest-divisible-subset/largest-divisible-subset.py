class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        size = len(nums)
        dp = [1] * size
        prev = [-1] * size
        maxi, mx = 0, 0

        for i in range(size):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    prev[i] = j
            if dp[i] > mx:
                mx = dp[i]
                maxi = i
        
        res = []

        while maxi != -1:
            res.append(nums[maxi])
            maxi = prev[maxi]

        return res