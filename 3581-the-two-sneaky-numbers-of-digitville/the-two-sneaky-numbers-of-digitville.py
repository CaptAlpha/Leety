class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                ans.append(i)
                if len(ans) == 2:
                    return ans

        return ans