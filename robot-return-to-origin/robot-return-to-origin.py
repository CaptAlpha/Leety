class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l, r = 0, 0
        u, d = 0, 0
        for i in moves:
            if i =='U': u+=1
            elif i == 'D': d+=1
            elif i == 'L': l+=1
            elif i == 'R': r+=1

        return l==r and d==u
