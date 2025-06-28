class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Keep the top k elements along with their original indices
        indexed = list(enumerate(nums))
        top_k = sorted(indexed, key=lambda x: x[1], reverse=True)[:k]
        top_k.sort(key=lambda x: x[0])  # Maintain original order
        return [x[1] for x in top_k]
