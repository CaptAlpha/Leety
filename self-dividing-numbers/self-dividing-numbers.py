class Solution:
    def selfDivide(self, n):
        s = str(n)
        s = list(s)

        for i in s:
            if int(i) == 0:
                return False
            if n % int(i) != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left, right+1):
            if self.selfDivide(i):
                arr.append(i)
        return arr