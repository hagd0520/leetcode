class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0

        def seek(x, y):
            
            if grid[x][y] == "0":
                return
            
            grid[x][y] = "0"
            
            if (x - 1) >= 0:
                seek(x - 1, y)
                
            if (x + 2) <= len(grid):
                seek(x + 1, y)
                
            if (y - 1) >= 0:
                seek(x, y - 1)
                
            if (y + 2) <= len(grid[x]):
                seek(x, y + 1)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    answer += 1
                    seek(i, j)
                    
        return answer