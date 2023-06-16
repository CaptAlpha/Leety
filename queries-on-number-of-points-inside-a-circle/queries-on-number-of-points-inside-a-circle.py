import math
class Solution:
    def dist(self, x1, y1, x2, y2):
        return math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))
    
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for i in queries:
            x = i[0]
            y = i[1]
            r = i[2]
            count = 0
            for j in points:
                x2 = j[0]
                y2 = j[1]
                if self.dist(x, y, x2, y2) <= r:
                    count += 1
            ans.append(count)
        return ans
