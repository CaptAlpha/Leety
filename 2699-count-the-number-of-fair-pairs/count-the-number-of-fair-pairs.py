class Solution:
    def lowerBound(self,nums: List[int],start: int, end: int, target: int):
        mid=0
        while start<end:
            mid=(start+end)//2
            if target>nums[mid]:
                start=mid+1
            else:
                end=mid
        
        return start
    
    def upperBound(self,nums: List[int],start: int, end: int, target: int):
        mid=0
        while start<end:
            mid=(start+end)//2
            if target>=nums[mid]:
                start=mid+1
            else:
                end=mid
        return start
    
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        count=0
        nums.sort()
        for i in range(0,len(nums)-1):
            minReq=lower-nums[i]
            maxReq=upper-nums[i]
            lowerB=self.lowerBound(nums,i+1,len(nums),minReq)
            upperB=self.upperBound(nums,i+1,len(nums),maxReq)
            print(lowerB,upperB)
            count+=upperB-lowerB
        return count