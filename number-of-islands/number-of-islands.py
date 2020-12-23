class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            grid[i][j] = "0"
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0]):
                    if grid[i+di][j+dj] == "1":
                        dfs(i+di, j+dj)
        
        count = 0
        
        for idx in range(len(grid)):
            for jdx in range(len(grid[0])):
                if grid[idx][jdx] == "1":
                    count += 1                    
                    dfs(idx, jdx)
                    
        return count
