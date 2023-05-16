class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_dic = {}
        for i in allowed:
            if i not in allowed_dic:
                allowed_dic[i] = 1
            else:
                allowed_dic += 1
        counter  = len(words)
        for i in words:
            for j in i:
                if j not in allowed_dic:
                    counter-=1
                    break
            

        return counter