from collections import Counter 
class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        t = []
        res = ""
        minchar = 'a'
        for c in s:
            t.append(c)
            cnt[c]-=1
            while minchar != 'z' and cnt[minchar] == 0:
                minchar = chr(ord(minchar)+1)
            while t and t[-1] <= minchar:
                res+=t.pop()
        return res
        
