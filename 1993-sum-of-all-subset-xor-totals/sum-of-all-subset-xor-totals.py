class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor_sum(arr):
            s = 0
            for i in arr:
                s^=i
            return s
        def generate_subarrays(arr):
            def generate(index, ans, ds, arr):
                if len(arr) == index:
                    ans.append(ds[:])
                    return
                ds.append(arr[index])
                generate(index+1, ans, ds, arr)
                ds.pop()
                generate(index+1, ans, ds, arr)

            ans = []
            ds = []
            generate(0, ans, ds, arr)
            return ans

        subsets = generate_subarrays(nums)
        print(subsets)

        ms = 0

        for i in subsets:
            ms+=xor_sum(i)
        return ms

        
