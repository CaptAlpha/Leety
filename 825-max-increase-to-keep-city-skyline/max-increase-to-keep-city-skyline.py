from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxRow = [max(row) for row in grid]
        maxCol = [max(col) for col in zip(*grid)]

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                counter += min(maxRow[i], maxCol[j]) - grid[i][j]

        return counter
