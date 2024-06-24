class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        ans = []
        for i in candies:
            if (i + extraCandies >= highest):
                ans.append(True)
            
            else:
                ans.append(False)
            
        return ans
        