class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: 
                continue
            t = 0 - nums[i]
            hashMap = {}
            j=i+1
            while(j<len(nums)):
                if t - nums[j] in hashMap:
                    res.append([nums[i],nums[j],t-nums[j]])
                    while (j+1<len(nums) and nums[j]==nums[j+1]):
                        j=j+1
                hashMap[nums[j]]=j
                j=j+1
        return res