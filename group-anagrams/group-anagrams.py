class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            key = sorted(i)
            key = "".join(key)
            if key in dic:
                dic[key].append(i)
            else:
                dic[key] = [i]
        print(dic)
        res = []
        for i in dic.values():
            res.append(i)
        return res
