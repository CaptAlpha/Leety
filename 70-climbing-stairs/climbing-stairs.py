class Solution:
    def climbStairs(self, n: int) -> int:

        def jump(n, dp):
            # if n == 1:
            #     return 1
            # if n == 0:
            #     return 1
            if dp[n]!=-1:
                return dp[n]
            else:
                dp[n] = jump(n-1, dp) + jump(n-2, dp)

            return dp[n]
        dp = [-1 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        return jump(n, dp)