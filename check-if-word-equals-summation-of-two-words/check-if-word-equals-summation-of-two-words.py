class Solution:
    def toString(self, s):
        dic = {}
        for i in range(10):
            dic[chr(97+i)] = str(i)
        num = ""
        for i in s:
            num+=dic[i]
        return int(num)
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f = self.toString(firstWord)
        s =  self.toString(secondWord)

        t =  self.toString(targetWord)
        return f+s==t
        