class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        r = n - index - 1 
        l = index 
        start, end = 0, maxSum
        ans = 1 
        while start <= end:
            mid = (start + end)//2
            sm = mid
            lsum, rsum = 0, 0
            m = mid - 1
            if r<=m: rsum = m*(m+1)//2 - (m-r)*(m-r+1)//2
            else: rsum = m*(m+1)//2 + r-m
            if l<=m: lsum = m*(m+1)//2 - (m-l)*(m-l+1)//2
            else: lsum = m*(m+1)//2 + l-m

            sm += lsum + rsum 
            if sm <= maxSum:
                ans = mid
                start = mid+1
            else: end = mid - 1
        return ans