class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        for i in range(n):
            arr.append((2 * i) + 1)
        counter = 0
        for i in arr[:n//2]:
            counter+=abs(n-i)
        return counter
        


