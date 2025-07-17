class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        res = 0
        ln = len(nums)
        dp = [[1]*ln for i in range(k)]

        for i in range(ln):
            for j in range(i):
                rem = (nums[j]+nums[i]) % k
                dp[rem][i] = max(dp[rem][j] + 1,dp[rem][i])
                res = max(res,dp[rem][i])
            
        return res
