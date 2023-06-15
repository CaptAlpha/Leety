class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        res= []
        for j in dic.values():
            res.append(j)
        
        for i in range(len(res)-1):
            if res[i] != res[i+1]:
                return False
        return True
            
