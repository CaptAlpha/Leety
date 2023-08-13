class Solution:
    def checkString(self, s: str) -> bool:
        la, fb = -1, len(s)  
        for i in range(len(s)):
            if s[i] == 'a':
                la = i

        for i in range(len(s)):
            if s[i] == 'b':
                fb = i
                break

        return la < fb
