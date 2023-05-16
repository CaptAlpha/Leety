class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        li = []
        for i in range(len(names)):
            if heights[i] not in dic:
                dic[heights[i]] = names[i]


        keys = list(dic.keys())
        keys.sort()
        keys = keys[::-1]

        for i in keys:
            li.append(dic[i])

        return li

        