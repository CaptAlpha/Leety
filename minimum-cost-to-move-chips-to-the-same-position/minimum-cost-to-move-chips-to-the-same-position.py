class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        dic = {}
        dic[0], dic[1] = 0, 0
        for i in position:
            dic[i%2] += 1
        return min(dic[0], dic[1])