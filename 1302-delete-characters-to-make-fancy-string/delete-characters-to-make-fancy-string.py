class Solution:
    def makeFancyString(self, s: str) -> str:
        charlist = []
        for i in s:
            if len(charlist) >= 2 and charlist[-1] == charlist[-2] == i:
                continue
            charlist.append(i)
        return ''.join(charlist) 


        