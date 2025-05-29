class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        

        heap = [(abs(n-x),n) for n in arr]

        heapify(heap)

        res = []
        for _ in range(k):

            res.append(heappop(heap)[1])
        
        res.sort()
        return res
