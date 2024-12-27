class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ans = []
        if strs == [""]:
            return [[""]]
        for i in strs:
            s = "".join(sorted(i))
            if s in dic:
                dic[s].append(i)
            else:
                dic[s] = [i]
        for i in dic.values():
            ans.append(i)
        return ans