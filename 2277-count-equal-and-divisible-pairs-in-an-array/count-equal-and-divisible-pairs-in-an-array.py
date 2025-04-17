class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        idx = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] not in idx:
                idx[nums[i]].append(i)
            else:
                for ix in idx[nums[i]]:
                    if ix*i % k == 0:
                        count += 1
                idx[nums[i]].append(i)
                
        return count