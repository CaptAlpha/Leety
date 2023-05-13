class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = 0
        m = 0
        for i in s:
            if i=='L':
                n+=1
            else:
                n-=1
            if n==0:
                m +=1

        return m


        