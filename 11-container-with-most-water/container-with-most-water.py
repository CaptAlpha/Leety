class Solution:
    def maxArea(self, height: List[int]) -> int:
        heights = height
        l = 0
        r = len(heights) - 1

        mA = -1

        while(l < r):
            area = (r-l) * min(heights[l],heights[r])

            if (heights[l]>heights[r]):
                r-=1
            else:
                l+=1

            mA = max(mA, area)
        return mA

        