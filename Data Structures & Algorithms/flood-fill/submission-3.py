class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        i_color = image[sr][sc]
        self.dfs(image, sr, sc, i_color, color)
        return image
    
    def dfs(self, image: List[List[int]], r: int, c: int, i_color: int, color: int):
        
        ROW, COL = len(image), len(image[0])

        if min(r,c) < 0 or r == ROW or c == COL or image[r][c] == color or image[r][c]!= i_color:
            return
        
        image[r][c] = color

        self.dfs(image, r, c + 1, i_color, color)
        self.dfs(image, r, c - 1, i_color, color)
        self.dfs(image, r + 1, c, i_color, color)
        self.dfs(image, r - 1, c, i_color, color)




        

        