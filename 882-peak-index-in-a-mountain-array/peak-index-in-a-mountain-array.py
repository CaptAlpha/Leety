class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) <= 2:
            return arr.index(max(arr))
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                return i
        return arr.index(max(arr))
