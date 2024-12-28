class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        aset = set(allowed)
        for i in words:
            sset = set(i)
            flag = True
            for j in sset:
                if j not in aset:
                    flag = False
            if flag: ans+=1 
        return ans
