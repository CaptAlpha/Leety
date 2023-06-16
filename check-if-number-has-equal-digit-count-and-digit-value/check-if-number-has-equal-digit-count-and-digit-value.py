class Solution:
    def digitCount(self, num: str) -> bool:
        n = len(num)
        for i in range(n):
            digit = int(num[i])
            count = num.count(str(i))
            if digit != count:
                return False
        return True