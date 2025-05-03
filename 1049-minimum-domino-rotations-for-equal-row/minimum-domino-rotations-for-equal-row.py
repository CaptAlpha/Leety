class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        n = len(tops)
        def getMaxKey(mpp, val):
            for i in mpp:
                if mpp[i] == val:
                    return i
        
        c1, c2 = Counter(tops), Counter(bottoms)
        m1, m2 = max(c1.values()), max(c2.values())
        k1, k2 = getMaxKey(c1, m1), getMaxKey(c2, m2)
        indices1, indices2 = [], []

        # check for array1
        for ind, val in enumerate(tops):
            if val != k1:
                indices1.append(ind)
        
        for ind, val in enumerate(bottoms):
            if val != k2:
                indices2.append(ind)
        
        # swap 1st array for just indices1
        temp1 = [domino for domino in tops]
        temp2 = [domino for domino in bottoms]
        swaps1 = 0
        for ele in range(len(indices1)):
            ind = indices1[ele]
            temp1[ind], temp2[ind] = temp2[ind], temp1[ind]
            swaps1 += 1
        
        allEqual1 = all(x == temp1[0] for x in temp1)
        
        # swap 2nd array for just indices2
        swaps2 = 0
        for ele in range(len(indices2)):
            ind = indices2[ele]
            bottoms[ind], tops[ind] = tops[ind], bottoms[ind]
            swaps2 += 1
        
        allEqual2 = all(x == bottoms[0] for x in bottoms)
        
        if not allEqual1 and not allEqual2:
            return -1
        
        if allEqual1 and not allEqual2:
            return swaps1

        if not allEqual1 and allEqual2:
            return swaps2
        
        if allEqual1 and allEqual2:
            return min(swaps1, swaps2)


        




        
