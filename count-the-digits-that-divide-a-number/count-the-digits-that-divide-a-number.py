class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        s = list(s)
        counter=0
        for i in s:
            counter = counter+1 if num%(int(i))==0 else counter

        return counter