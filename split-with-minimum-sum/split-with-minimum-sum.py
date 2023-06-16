class Solution:
    def splitNum(self, num: int) -> int:
        even, odd = "", ""
        s = list(str(num))
        s.sort()
        for i in range(len(s)):
            if i%2:
                odd+=s[i]
            else:
                even+=s[i]

        return int(even)+int(odd)