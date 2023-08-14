class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = list(set(nums))
        m = int(len(nums)/3)
        ans = []
        for i in n:
            if nums.count(i) > m:
                ans.append(i)
        return ans