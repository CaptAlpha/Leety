class Solution:
    def countAsterisks(self, s: str) -> int:
        curr = 0
        ast = 0
        for i in s:
            if i == '|':
                curr+=1 
            if curr%2==0:
                if i == "*":
                    ast+=1

        return ast  