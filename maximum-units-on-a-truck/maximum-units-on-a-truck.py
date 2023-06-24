class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        dic = {}

        for i in boxTypes:
            box = i[0]
            units = i[1]
            if units in dic:
                dic[units] += box
            else:
                dic[units] = box
        # Sort the boxes on the units
        keys = dic.keys()
        keys = list(keys)
        keys.sort(reverse=True)

        new = {}
        for i in keys:
            new[i] = dic[i]
        print(new)
        maxUnits = 0
        for i, j in new.items():

            for k in range(j):
                if truckSize>0:
                    truckSize -= 1
                    maxUnits += i
                else:
                    break
        return maxUnits
