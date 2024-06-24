class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richestWealth = 0
        for i in accounts:
            richestWealth = max(sum(i), richestWealth)
        return richestWealth
        