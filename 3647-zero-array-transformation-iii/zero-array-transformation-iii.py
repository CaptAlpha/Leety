import heapq
from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        candidates = []
        chosen = []

        for i in range(len(nums)):
            while queries:
                x, y = queries.pop(0)
                if x == i:
                    heapq.heappush(candidates, -y)
                else:
                    queries.insert(0, [x, y])
                    break
            
            reqd = nums[i] - len(chosen)

            if len(candidates) < reqd:
                return -1
            while reqd > 0 and candidates:
                ele = -heapq.heappop(candidates)
                if ele < i:
                    continue
                heapq.heappush(chosen, ele)
                reqd -= 1

            nums[i] -= len(chosen)

            if nums[i] > 0:
                return -1
            
            while chosen:
                ele = heapq.heappop(chosen)
                if ele != i:
                    heapq.heappush(chosen, ele)
                    break

        return len(queries) + len(candidates)