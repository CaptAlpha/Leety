class Solution:
    def findCombos(self, ind, candidates, target, ans, ds):
        #Base Condition
        if(ind == len(candidates)):
            if(target==0):
                ans.append(ds[:])

            return 

        if(target>=candidates[ind]):
            ds.append(candidates[ind])
            self.findCombos(ind, candidates, target-candidates[ind], ans, ds)
            ds.pop()

            

        self.findCombos(ind+1, candidates, target, ans, ds)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans  = []
        ds = []
        ind = 0

        self.findCombos(ind, candidates, target, ans, ds)

        return ans


