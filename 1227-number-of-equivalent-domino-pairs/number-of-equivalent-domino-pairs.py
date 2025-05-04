class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashMap = {}
        for i in dominoes:
            i.sort()
            x = str(i)
            if x not in hashMap:
                hashMap[x] = 1
            else:
                hashMap[x] +=1
        print(hashMap)
        count = 0
        for i in hashMap.values():
            count += (i*(i-1))//2
        return count