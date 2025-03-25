class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]
        for i, j in intervals[1:]:
            if  stack[-1][1] >= i:
                j = max(stack[-1][1], j)
                stack[-1][1] = j
            else:
                stack.append([i, j])
        return stack