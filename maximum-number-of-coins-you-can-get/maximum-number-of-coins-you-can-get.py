class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n =  len(piles)//3
        piles.sort()
        counter = 0
        for i in range(n, len(piles), 2):
            counter+=piles[i]
        return counter




