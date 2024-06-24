class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in accounts:
            money = 0
            for j in i:
                money += j
            if money > wealth:
                wealth = money
        return wealth
        