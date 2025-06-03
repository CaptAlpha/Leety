from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n, ans = len(status), 0
        queue, seen, owned, has_key = deque(), set(), set(initialBoxes), set()
        
        for box in initialBoxes:
            if status[box]: queue.append(box)
        
        while queue:
            box = queue.popleft()
            if box in seen: continue
            seen.add(box)
            ans += candies[box]
            for k in keys[box]:
                if k not in has_key:
                    has_key.add(k)
                    if k in owned and k not in seen:
                        queue.append(k)
            for b in containedBoxes[box]:
                owned.add(b)
                if status[b] or b in has_key:
                    queue.append(b)
        
        return ans