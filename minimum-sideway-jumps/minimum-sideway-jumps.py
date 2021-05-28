class Solution:
    def minSideJumps(self, A: List[int]) -> int:
        
        # 1 - overall init
        dp = [
            [float('inf')] * 4      # "lane" parameter
            for _ in range(len(A))  # "idx" parameter
        ]
        
        # 2 - first item init
        dp[0] = [float('inf'), 1, 0, 1]
        
        # 3 - loop
        for i in range(1, len(A)):  # loops usually start at 1, not 0                                    
            
            # 4                        
            for j in range(1, 4):                
                dp[i][j] = dp[i-1][j] if A[i] != j else float('inf')
            for j in range(1, 4):
                if j == A[i]: continue
                dp[i][j] = min(
                    min(dp[i])+1,
                    dp[i][j]
                )                         
        
        # 5
        return min(dp[-1])
    
"""
Top down idea:
- Memory limit exceeds :0
- Easy to come up with thou

```python
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
                                
        @functools.lru_cache(None)
        def recurse(idx, lane):                    
            if idx >= len(obstacles): return 0            
            if obstacles[idx] == lane: return float('inf')            
            return min([
                (1 if l != lane else 0) + recurse(idx+1, l)
                for l in range(1, 4)
                if l != obstacles[idx]
            ])
        
        return recurse(0, 2)
```
"""
        
            