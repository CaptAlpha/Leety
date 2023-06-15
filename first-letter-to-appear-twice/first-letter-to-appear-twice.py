class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic= {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                if dic[i] == 2:
                    return i
        return ""
        