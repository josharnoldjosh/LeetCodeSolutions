class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
           
        N, M = len(grid), len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_heap = [(-grid[0][0], 0, 0)]
        seen = set()
        
        while max_heap:
            val, i, j = heapq.heappop(max_heap)
            
            if (i, j) == (N-1, M-1): return -val
            
            for di, dj in delta:
                ni, nj = i+di, j+dj                
                if not (0 <= ni < N): continue
                if not (0 <= nj < M): continue
                if (ni, nj) in seen: continue     
                    
                seen.add((ni, nj))                
                heapq.heappush(
                    max_heap,                     
                    (
                        max(val, -grid[ni][nj]), 
                        ni, 
                        nj
                    )
                )
                        
        return -1
        
        
            
    
"""
Backtracking (TLE):
```python
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        N, M = len(grid), len(grid[0])
        
        seen = set([(0, 0)])
        path = [grid[0][0]]
        results = []
        
        def backtrack(i, j):
                                    
            # Termination
            if i == N-1 and j == M-1: return True
            
            # Loop                        
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:                       
                
                if (i+di, j+dj) in seen: continue
                if not (0 <= i+di < N): continue
                if not (0 <= j+dj < M): continue
                                                                            
                seen.add((i, j))                
                path.append(grid[i+di][j+dj])
                
                if backtrack(i+di, j+dj):
                    results.append(min(path))
                    
                path.pop()
                seen.remove((i, j))                            
                                            
        backtrack(0, 0)
        return max(results)
```

"""