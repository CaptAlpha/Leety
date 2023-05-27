class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)


        for _ in range(3):
            m = -9223372036854775807
            for i in nums:
                m = max(m, i)

            for i in range(len(nums)):
                if nums[i] == m:
                    nums[i] = -9223372036854775807

        for i in nums:
            m = max(m, i)

        return m

