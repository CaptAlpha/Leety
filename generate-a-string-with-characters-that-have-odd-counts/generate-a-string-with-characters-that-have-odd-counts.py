class Solution:
    def generateTheString(self, n: int) -> str:
        word = "a"*(n-1)
        if n%2==1:
            word  += "a"
        else:
            word+="b"

        return word