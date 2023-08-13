class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr = []
        charArray = []
        for i in range(len(s)):
            if s[i] == c:
                charArray.append(i)
        for i in range(len(s)):
            n = 10000
            for j in charArray:
                n = min(n, abs(j - i))
            arr.append(n)
        return arr

