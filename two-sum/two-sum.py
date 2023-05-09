class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = target - i
        li = []
        for i in range(len(nums)):
            if dic[nums[i]] in nums and nums.index(dic[nums[i]])!=i:
                li.append(i)
                li.append(nums.index(dic[nums[i]]))
                break

        return li


        
