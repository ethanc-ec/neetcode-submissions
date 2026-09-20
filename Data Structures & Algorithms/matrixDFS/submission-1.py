class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = {}
        return self.dfs(grid, 0, 0, visit)
        
    
    def dfs(self, grid: List[List[int]], r, c, visit: dict[[tuple[int, int]], int]):
        ROW, COL = len(grid), len(grid[0])
        if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] == 1 or (r,c) in visit:
            return 0

        #base case, the end is reached
        if r == ROW - 1 and c == COL - 1:
            return 1
        
        visit[(r,c)] = 1
        #visit lower down
        count = 0

        count += self.dfs(grid, r, c + 1, visit)    
        count += self.dfs(grid, r, c - 1, visit)  
        count += self.dfs(grid, r - 1, c, visit)    
        count += self.dfs(grid, r + 1, c, visit)    

        visit.pop((r,c))
        return count 
   
        
        

        