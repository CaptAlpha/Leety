from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0  # No water can be trapped if there are fewer than 3 bars
        
        n = len(height)
        mL = [0] * n  # Maximum height to the left of each bar
        mR = [0] * n  # Maximum height to the right of each bar
        
        # Calculate mL
        mL[0] = height[0]
        for i in range(1, n):
            mL[i] = max(mL[i - 1], height[i])
        
        # Calculate mR
        mR[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            mR[i] = max(mR[i + 1], height[i])
        
        # Calculate trapped water
        total_water = 0
        for i in range(n):
            total_water += max(0, min(mL[i], mR[i]) - height[i])
        
        return total_water

