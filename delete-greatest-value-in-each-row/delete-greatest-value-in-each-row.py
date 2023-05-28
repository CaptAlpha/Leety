
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        while grid:
            max_values = []
            for row in grid:
                max_value = max(row)
                max_values.append(max_value)
                row.remove(max_value)
            
            ans += max(max_values)
            grid = [row for row in grid if row]
        
        return ans
