class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        for i in range(len(nums)):
            target = -(nums[i])
            d={}
            for j in range(i+1,len(nums)):
                if target - nums[j] in d:
                    triplets.append(sorted([nums[i],target-nums[j],nums[j]]))
                else:
                    d[nums[j]]=j
                    
        return sorted(list(set(map(tuple,triplets))))