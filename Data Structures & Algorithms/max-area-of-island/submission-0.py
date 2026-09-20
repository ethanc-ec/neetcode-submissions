class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max = 0
        ROW, COL = len(grid), len(grid[0])

        def dfs(m, n):
            if min(m,n) < 0 or m == ROW or n == COL or grid[m][n] == 0:
                return 0

            grid[m][n] = 0

            count = 1
            count += dfs(m, n + 1)
            count += dfs(m, n - 1)
            count += dfs(m + 1, n)            
            count += dfs(m - 1, n)   

            return count  
        
        for i in range(0, ROW):
            for j in range (0, COL):
                if grid[i][j] == 1:
                    curr = dfs(i,j)
                    if curr > max:
                        max = curr
        return max
               