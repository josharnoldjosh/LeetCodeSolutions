class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def backtrack(i, j, result=0):
            if not 0 <= i < len(grid): return result
            if not 0 <= j < len(grid[0]): return result
            if (i, j) in seen: return result
            if grid[i][j] == 0: return result
            
            seen.add((i, j))
            result += grid[i][j]
            mx = 0
                                
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:            
                mx = max(mx, backtrack(x, y, result))
                
            seen.remove((i, j))
        
            return mx
        
        
        
        seen = set()        
        result = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: continue
                result = max(result, backtrack(i, j))
                
        return result
            
        