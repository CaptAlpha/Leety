class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        def check(nums):
            for i in nums: 
                if nums.count(i) > 1:
                    return False
            return True
        def rec(nums, count):
            if check(nums): return count
            count += 1
            if len(nums) < 3: return count
            
            return rec(nums[3:], count)
        
        return rec(nums, 0)