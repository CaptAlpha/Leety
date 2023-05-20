class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        val = list(dic.values())
        m = max(val)

        for i, j in dic.items():
            if j == m:
                return i

        return -1

        
            

        