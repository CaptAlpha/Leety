class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        m = 0
        area = 0
        while(left<right):
            a = min(height[left], height[right])
            b = abs(right-left)

            area=a*b

            m = max(area, m)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return m



