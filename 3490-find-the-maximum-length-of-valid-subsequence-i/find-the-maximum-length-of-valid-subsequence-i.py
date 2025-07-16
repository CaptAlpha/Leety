class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        l, r, n = 0, 1, len(nums)
        maxlen = odds = evens = 0

        if nums[0] % 2 == 1:
            isNextEven = 1
            odds += 1
        else:
            isNextEven = 0
            evens += 1

        while r < n:
            if nums[r] % 2 == 1:
                odds += 1
            else:
                evens += 1

            if nums[r] % 2 == isNextEven:
                maxlen += r - l
                l = r + 1
            else:
                isNextEven = 1 - isNextEven

            r += 1

        maxlen += r - l
        return max(maxlen, max(odds, evens))