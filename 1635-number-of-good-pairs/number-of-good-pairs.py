class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        print(count)

        p = 0

        for key in count:
            p = p + (count[key]*(count[key]-1)) // 2

        return p
        