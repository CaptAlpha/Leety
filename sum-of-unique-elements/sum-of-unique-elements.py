class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic= {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1

        s = 0
        for i, j in dic.items():
            if j == 1:
                s+=i
        return s