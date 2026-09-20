class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        ROW, COL = len(grid), len(grid[0])

        def dfs(grid: List[List[str]], r: int, c: int):
            if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] == '0':
                return
            
            grid[r][c] = '0' 

            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            

        for i in range (0, ROW):
            for j in range (0, COL):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        
        return count

            
    
