class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [i]
            else:
                dic[s[i]].append(i)
        print(dic)

        partition = {}

        for i, j in dic.items():
            partition[i] = j[-1] 
        res= []
        end, size = 0, 0
        for i, c in enumerate(s):
            size += 1

            end = max(end, partition[c])

            if i == end:
                res.append(size)
                size = 0
        return res
