class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([value, timestamp])
        else:
            self.map[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        # Perform binary search to find the largest timestamp <= target
        values = self.map[key]
        left, right = 0, len(values) - 1
        res = ""
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
                
        return res