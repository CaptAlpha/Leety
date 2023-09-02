class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        arr = []
        for i in range(n+1):
            arr.append(0)
        arr[0] = 0
        for i in range(1, n+1):
            if arr[i] is not None:
                arr[i] = arr[i-1]+1
            for j in range(i):
                if s[j:i] in dictionary and s[j:i] != None:
                    arr[i] = min(arr[i], arr[j])
                    
        return arr[n]
        