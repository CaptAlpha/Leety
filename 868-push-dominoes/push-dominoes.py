class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        i = 0
        L = 0
        R = 0
        domioes = [a for a in dominoes]
        while i < len(domioes):
            while R<len(domioes) and dominoes[R] == ".":
                R+=1
            i = R+1
            if L-1 >= 0 and R<len(domioes):
                if domioes[L-1] == "R" and domioes[R] == "R":
                    while L<R:
                        domioes[L] = "R"
                        L+=1
                elif domioes[L-1] == "L" and domioes[R] == "R":
                    pass
                    
                elif domioes[L-1] == "L" and domioes[R] == "L":
                    while L<R:
                        R-=1
                        domioes[R] = "L"
                elif domioes[L-1] == "R" and domioes[R] == "L":
                    while L<R-1:
                        R-=1
                        domioes[R] = "L"
                        domioes[L] = "R"
                        L+=1
            elif L == 0 and R<len(domioes):
                if domioes[R] == "L":
                    while L<R:
                        R-=1
                        domioes[R] = "L"
            elif R == len(domioes) and L!=0:
                if domioes[L-1] == "R":
                    while L<R:
                        domioes[L] = "R"
                        L+=1
            L = i
            R = L

        return "".join(domioes)