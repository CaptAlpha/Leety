class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for item in items1:
            if item[0] in dic:
                dic[item[0]] += item[1]
            else:
                dic[item[0]] = item[1]
        for item in items2:
            if item[0] in dic:
                dic[item[0]] += item[1]
            else:
                dic[item[0]] = item[1]
        print(dic)
        ret = []
        myKeys = list(dic.keys())
        myKeys.sort()
        sorted_dict = {i: dic[i] for i in myKeys}
        for i, j in sorted_dict.items():
            ret.append([i, j])
        return ret