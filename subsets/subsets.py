class Solution:
    def findCombo(self, ind, nums, ds, ans):
        if ind == len(nums):
            ans.append(ds[:])
            return 

        ds.append(nums[ind])
        self.findCombo(ind+1, nums, ds, ans)
        ds.pop()
        self.findCombo(ind+1, nums, ds, ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        ind = 0

        self.findCombo(ind, nums, ds, ans)

        return ans