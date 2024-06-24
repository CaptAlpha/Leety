class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        maxVH = 0
        # mark all points which are at same height
        same = []
        for i in range(len(points)-1):
           
            maxVH = max(maxVH, points[i+1][0] - points[i][0])
        return maxVH



      