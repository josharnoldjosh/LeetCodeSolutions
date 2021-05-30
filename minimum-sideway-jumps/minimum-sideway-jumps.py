class Solution:
    def minSideJumps(self, A: List[int]) -> int:
        
        # 1
        N = len(A) - 1        
        dp = [
            [float('inf')] * 3
            for _ in range(N)
        ]
        
        # 2
        dp[0] = [1, 0, 1]
        
        # 3
        for i in range(1, N):
            for j in range(3):
                
                # 4
                if j+1 in {A[i], A[i+1]}:
                    dp[i][j] = float('inf')
                else:
                    dp[i][j] = min(
                        dp[i-1][0] + (1 if j != 0 else 0),
                        dp[i-1][1] + (1 if j != 1 else 0),
                        dp[i-1][2] + (1 if j != 2 else 0),
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

Bottom up!
```python
class Solution:
    def minSideJumps(self, A: List[int]) -> int:
                        
        N = len(A) - 1
            
        dp = [
            [float('inf')] * 3
            for _ in range(N)
        ]
        
        dp[0] = [1, 0, 1]
        
        for i in range(1, N):
            for j in range(3):
            
                # This line here is the tricky one                
                if A[i] == j+1 or A[i+1] == j+1:
                    dp[i][j] = float('inf')
                else:
                    dp[i][j] = min([
                        dp[i-1][0] + (1 if j != 0 else 0),
                        dp[i-1][1] + (1 if j != 1 else 0),
                        dp[i-1][2] + (1 if j != 2 else 0),
                    ])
                    
        return min(dp[-1])
```
"""
        
            