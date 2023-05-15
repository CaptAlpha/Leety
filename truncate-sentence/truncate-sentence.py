class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        p = ""
        s = s.split(" ")
        for i in range(k-1):
            p+=s[i]
            p+=" "
        p+=s[k-1]

        return p
        
