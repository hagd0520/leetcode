class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0

        def seek(x, y):
            
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "0" :
                return
            
            grid[x][y] = "0"
            
            seek(x - 1, y)
            seek(x + 1, y)
            seek(x, y - 1)
            seek(x, y + 1)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    answer += 1
                    seek(i, j)
                    
        return answer