class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        # for k in range(len(grid)):
        for i in range(1, len(grid)-1, 1):
            arr = []
            for j in range(1, len(grid)-1, 1):
                # print(grid[i][j], end=" ")
                # Find the max of the nearby elements
                

                m = (max(
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],  # top-left, top, top-right
                    grid[i][j-1],  grid[i][j],               grid[i][j+1],    # left,       right
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]   # bottom-left, bottom, bottom-right
                ))
                print(m)
                arr.append(m)
                print(arr)
            print()
            ans.append(arr)
        return ans
        