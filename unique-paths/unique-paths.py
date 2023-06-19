class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dic = {(1, 1): 1}

        def rec(m, n):
            if m == 0 or n == 0:
                return 0
            if (m, n) in dic:
                return dic[(m, n)]
            
            dic[(m, n)] = rec(m-1, n)+ rec(m, n-1)

            return dic[(m,n)]
        
        return rec(m,n)