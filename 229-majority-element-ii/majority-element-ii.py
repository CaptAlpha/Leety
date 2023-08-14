class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        m = int(len(nums)/3)
        ans = set()
        for i in nums:
            if nums.count(i) > m:
                ans.add(i)
        k = list(ans)
        return k