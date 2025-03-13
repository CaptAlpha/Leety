class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1

        p = (n*(n-1))//2

        flag = 0

        for i in nums:
            p-=i
            if i == 0:
                flag = 1
        
        if flag == 0: return 0

        return p if p!=0 else len(nums)
