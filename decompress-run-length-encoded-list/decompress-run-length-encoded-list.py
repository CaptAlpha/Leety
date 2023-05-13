class Solution:
    def createList(self, freq, val):
        return [val]*freq
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            li += self.createList(freq, val)

        return li