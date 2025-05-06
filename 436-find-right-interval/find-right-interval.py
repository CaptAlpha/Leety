class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Handle single interval case
        if len(intervals) == 1:
            if intervals[0][1] == intervals[0][0]: return [0]
            return [-1]

        ans = []
        h = {}  
        # Build hashmap
        for i in range(len(intervals)):
            h[intervals[i][0]] = i
        
        sorted_starts = sorted(h.keys())

        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            result = -1
            
            if target > arr[-1]:
                return -1

            while left <= right:
                mid = (left + right) // 2
                
                if arr[mid] == target:
                    return h[arr[mid]]
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    result = h[arr[mid]]
                    right = mid - 1
                    
            return result

        # Find right interval for each interval
        for interval in intervals:
            end = interval[1]
            right_idx = binary_search(sorted_starts, end)
            ans.append(right_idx)
        
        return ans