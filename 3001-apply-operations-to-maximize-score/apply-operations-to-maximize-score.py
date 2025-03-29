class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def helper(nums):
            arr = []
            for ele in nums:
                score = 0
                for i in range(2, int(sqrt(ele)) + 1):
                    if ele % i == 0:
                        score += 1
                        while ele % i == 0:
                            ele //= i
                if ele >= 2:
                    score += 1
                arr.append(score)
            return arr 
        
        arr = helper(nums)  # Get prime factor count array
        print(arr) 
        def stackify(arr):
            left = [-1] * n
            right = [n] * n
            st = []

            for i in range(n):
                while st and arr[st[-1]] < arr[i]:
                    right[st.pop()] = i
                if st:
                    left[i] = st[-1]
                st.append(i)

            return left, right

        left, right = stackify(arr)  # Get valid boundaries
        
        ans = 1
        MOD = 10**9 + 7  # To prevent overflow
        pq = []
        for i in range(n):
            heappush(pq, (-nums[i], i))

        while k > 0 and pq:
            ele, idx = heappop(pq)
            ele *= -1
            possible = (idx - left[idx]) * (right[idx] - idx)

            if possible >= k:
                ans = (ans * pow(ele, k, MOD)) % MOD
                break
            else:
                ans = (ans * pow(ele, possible, MOD)) % MOD
                k -= possible

        return ans