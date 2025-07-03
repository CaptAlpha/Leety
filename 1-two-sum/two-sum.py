class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, i in enumerate(nums):
            if i in dic:
                return [dic[i], index]
            dic[target - i] = index
        return [0, 0]