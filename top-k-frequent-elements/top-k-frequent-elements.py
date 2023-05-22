class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        # Create a heap to store the k most frequent elements.
        heap = []
        for num, frequency in frequencies.items():
            heapq.heappush(heap, (-frequency, num))

        # Get the k most frequent elements from the heap.
        results = []
        for _ in range(k):
            results.append(heapq.heappop(heap)[1])

        return results

        