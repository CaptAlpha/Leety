class Solution:
    def countPoints(self, rings: str) -> int:
        dic = {}
        counter = 0
        for i in range(0,len(rings)-1,2):
            color = rings[i]
            rod = rings[i+1]

            if rod not in dic:
                dic[rod] = [color]
            else:
                dic[rod].append(color)
        for i, j in dic.items():
            res = list(set(j))
            res.sort()
            if res == ['B', 'G', 'R']:
                counter+=1
        return counter


