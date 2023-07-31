class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxDiff = -1
        for i in range(len(points)-1):
            diff = (points[i][0] - points[i+1][0])*-1
            maxDiff = max(maxDiff, diff)
            print(maxDiff)
        return maxDiff

