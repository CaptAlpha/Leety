class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        main = {}
        counter=0
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                if j not in main:
                    main[j] = strs[i][j]
                else:
                    main[j] += strs[i][j]
        for i in main.values():
            for j in range(len(i)-1):
                if i[j] > i[j+1]:
                    counter+=1
                    break 
        return counter