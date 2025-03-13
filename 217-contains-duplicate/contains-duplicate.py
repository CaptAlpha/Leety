class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i in c.values():
            if i >= 2:
                return True
        return False