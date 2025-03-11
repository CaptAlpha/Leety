class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l = 0
        r = 1
        while(r < len(prices)):
            if (prices[l] >= prices[r]):
                l = r
            
            else:
                p += prices[r] - prices[l]
                l = r
            r+=1
        return p