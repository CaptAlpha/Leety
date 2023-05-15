class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = ((k-1)*k)//2
        return (max(nums)*k)+m