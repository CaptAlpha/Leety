class Solution:

    def xorarr(self, arr):
        n = 0
        if len(arr)==1:
            return arr[0]

        for i in arr:
            n^=i
            print(n)
        return n

    def findCombo(self, ind, arr, ds, ans ):
        if(ind==len(arr)):
            
            if len(ds)==0:
                ans.append([0])
                return
            ans.append(ds[:])
            return 
        ds.append(arr[ind])
        self.findCombo(ind+1, arr, ds, ans)
        ds.pop()
        self.findCombo(ind+1, arr, ds, ans)


    def subsetXORSum(self, nums: List[int]) -> int:
        ans = []
        ds = []
        ind = 0
        self.findCombo(ind, nums, ds, ans)
        s = 0
        print(ans)
        for i in ans:
            s+=self.xorarr(i)

        return s