class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dic = {}
        a = 64
        for i in range(1, 27):
            dic[chr(a+i)] = i
        print(dic)
        s = columnTitle[::-1]
        res = 0
        for i in range(len(s)):
            res+= (26**i)*dic[s[i]]
        return res





