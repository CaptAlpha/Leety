class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element = 0
        for i in nums:
            element += i
        digit = 0
        for i in nums:
            i = str(i)
            for j in i:
                digit+=int(j)

        return abs(element-digit)