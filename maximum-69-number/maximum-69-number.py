class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        s = list(s)
        res= ""
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                break
        for i in s:
            res+=(i)
        return int(res)