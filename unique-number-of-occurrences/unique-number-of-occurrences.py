class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        print(dic)
        print(len(set(dic.values())))
        print(len(arr))
        return len(dic) == len(set(dic.values()))