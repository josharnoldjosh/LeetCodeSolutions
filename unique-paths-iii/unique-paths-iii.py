class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        global result
        result = 0
                    
        def backtrack(i, j, squares):
            global result
            
            if not (0 <= i < len(grid)): return
            if not (0 <= j < len(grid[0])): return
            
            if grid[i][j] == -1: return # ignore obstacles
            
            if grid[i][j] == 2: # return
                if squares == 0:
                    result += 1 # only add result if we've reached all squares
                return             
            
            if grid[i][j] == 0:
                squares -= 1 # one less square to touch
                
            grid[i][j] = -1
                
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                backtrack(x, y, squares)
                
            grid[i][j] = 0
                
                                
        # 1. Figure out how many zeros we need?
        num_zeros = 0
        for i in grid:
            num_zeros += collections.Counter(i)[0]
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    backtrack(i, j, num_zeros)
        
        return result
    
    
"""
- walk over every "0"?
- do not walk over any -1
- start at 1
- end at 2
"""