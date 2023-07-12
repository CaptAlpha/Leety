class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dic:
                dic[groupSizes[i]] = [i]
            else:
                dic[groupSizes[i]].append(i)
        print(dic)

        ans = []

        for i, j in dic.items():
            if len(j) == i:
                ans.append(j)
            else:
                for k in range(0, len(j), i):
                    ans.append(j[k:k+i])

        return ans