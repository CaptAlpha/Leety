class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:

        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                dic[s[i]] = i - dic[s[i]] - 1

        for i in range(len(distance)):
            if chr(i+97) in dic:
                if dic[chr(i+97)] != distance[i]:
                    return False
        

        
        return True