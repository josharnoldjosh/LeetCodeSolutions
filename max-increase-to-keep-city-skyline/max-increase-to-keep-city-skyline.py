class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
                      
        grid_t, result = list(zip(*grid)), 0
        
        for i in range(len(grid)):            
            for j in range(len(grid[0])):
                max_height = min(max(grid[i]), max(grid_t[j]))
                update = max_height - grid[i][j]
                result += update                
                
        return result