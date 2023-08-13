class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        counter = 0
        arr = []
        for i in range(1, len(s)+1):
            if s[:i] in words:
                arr.append(s[:i])
        for i in words:
            if i in arr:
                counter+=1        
        return counter