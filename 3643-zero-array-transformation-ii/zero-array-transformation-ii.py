from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        if sum(nums) == 0: return 0
        left, right = 1, m
        result = -1

        while left <= right:
            mid = (left + right) // 2
            diff = [0] * (n + 1)
            for i in range(mid):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val
            possible = True
            current = 0
            for i in range(n):
                current += diff[i]
                if nums[i] - current > 0:
                    possible = False
                    break

            if possible:
                result = mid
                right = mid - 1 
            else:
                left = mid + 1  

        return result