class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        li = []
        if haystack == needle:
            return 0

        if len(needle)==1:
            for i in haystack:
                if i==needle:
                    return haystack.index(i)
                
            return -1
        for i in range(0, len(haystack)-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1

        