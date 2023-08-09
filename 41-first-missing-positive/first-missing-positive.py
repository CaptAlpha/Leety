class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x=[0]
        for i in sorted(set(nums)):
            if i>0 and i-x[-1]==1:
                x.append(i)
            elif i>0:
                return x[-1]+1
        return max(1,max(nums)+1)