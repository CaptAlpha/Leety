class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        p = 0
        while(j < len(prices)):
            if (prices[i] > prices[j]):
                i = j
            p = max((prices[j] - prices[i]), p)
            j+=1
        return p
        