class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)

        res = [intervals[0]]

        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]

            if start <= res[-1][1]:
                if end >= res[-1][1]:
                    res[-1][1] = end
            else:
                res.append(interval)
        return res
