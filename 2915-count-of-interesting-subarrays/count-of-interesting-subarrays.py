class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cnts = defaultdict(int)
        cnts[0] = 1
        ps, ans = 0, 0
        for num in nums:
            ps += int((num % modulo) == k)
            ans += cnts[(ps % modulo) - k + modulo] + cnts[(ps % modulo) - k]

            cnts[ps % modulo] += 1

        return ans