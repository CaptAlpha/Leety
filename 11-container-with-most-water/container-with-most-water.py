class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxArea = -1
        while(start <= end):
            currArea = (end - start)*(min(height[start], height[end]))
            maxArea = max(maxArea, currArea)

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return maxArea