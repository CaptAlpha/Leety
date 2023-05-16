class Solution:
    def sortSentence(self, s: str) -> str:
        dic={}
        for i in s.split(" "):
            dic[int(i[-1])] = i[:-1]

        keys = list(dic.keys())
        keys.sort()
        new = {}
        for i in keys:
            new[i] = dic[i]

        p = ""
        for i in new.values():
            p+=i
            p+=" "
        return p[:-1]