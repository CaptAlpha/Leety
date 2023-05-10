from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]  # Create a 2D list with separate rows

        counter = 1
        rows = n
        cols = n
        top = 0
        bottom = cols - 1
        right = rows - 1
        left = 0
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                m[top][i] = counter
                counter += 1
            top += 1

            for i in range(top, bottom + 1):
                m[i][right] = counter
                counter += 1
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    m[bottom][i] = counter
                    counter += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    m[i][left] = counter
                    counter += 1
                left += 1
        return m
