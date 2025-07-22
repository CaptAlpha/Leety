class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        window = {nums[0]: 0}
        sum_ = nums[0]
        max_ = sum_
        len_ = len(nums)
        while left < len_:
            while right < len_ - 1 and window.get(nums[right + 1], -1) < left:
                num = nums[right + 1]
                sum_ += num
                window[num] = right + 1
                right += 1
                max_ = max(max_, sum_)
            if right == len_ - 1:
                return max_
            while window.get(nums[right + 1]) >= left:
                num = nums[left]
                sum_ -= num
                left += 1
        return max_