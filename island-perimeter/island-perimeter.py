class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        M, N, result = len(grid), len(grid[0]), 0
                
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    result += sum([
                        grid[i+1][j] == 0 if 0 <= i+1 < M else 1,
                        grid[i-1][j] == 0 if 0 <= i-1 < M else 1,
                        grid[i][j+1] == 0 if 0 <= j+1 < N else 1,
                        grid[i][j-1] == 0 if 0 <= j-1 < N else 1,
                    ])
            
        return result
                
                
    
    
"""
Greedy -> find first island

DFS w/ visited to stop duplicate stuff

check if a coording is a perimiter or not
    -> i.e, count the number of zeros the coordinate is touching 
"""