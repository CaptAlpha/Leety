class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        arr = [i for i in range(1,n+1)]

        def backtrack(ind, arr, ds, ans, k):

            if ind == len(arr):
                if len(ds) == k:
                    ans.append(ds[:])
                return
            
            ds.append(arr[ind])
            backtrack(ind+1, arr, ds, ans, k)
            ds.pop()
            backtrack(ind+1, arr, ds, ans, k)

        ans = []
        ds = []
        ind = 0
        backtrack(ind, arr, ds, ans, k)

        return ans