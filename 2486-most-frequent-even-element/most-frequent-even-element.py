class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
            if i%2 == 0:
                dic[i] += 1
        # print(dic)
        if len(dic) == 0:
            return -1
        m = (list(dic.values()))
        maxCount = max(m)
        arr = []
        minElement = 10000000
        
        for i, j in dic.items():
            if j == maxCount:
                minElement = min(minElement, i)
        return minElement

            