class Solution:
    def minSideJumps(self, obs: List[int]) -> int:
        dp = [1000000, 1, 0, 1]
        for i in obs:
            dp[i] = dp[0]
            for j in range(1, 4):
                dp[j] = min(dp[1] + (1 if j != 1 else 0),
                           dp[2] + (1 if j != 2 else 0),
                           dp[3] + (1 if j != 3 else 0)) if j != i else dp[j]
        return min(dp)
"""

class Solution:
    def minSideJumps(self, obs: List[int]) -> int:
        dp = [1000000, 1, 0, 1]
        for i in obs:
            dp[i] = dp[0]
            for j in range(1, 4):
                dp[j] = min(dp[1] + (1 if j != 1 else 0),
                           dp[2] + (1 if j != 2 else 0),
                           dp[3] + (1 if j != 3 else 0)) if j != i else dp[j]
        return min(dp)


dp[i] = dp

    def minSideJumps(self, A):
        dp = [1, 0, 1]
        for a in A:
            if a:
                dp[a - 1] = float('inf')
            for i in xrange(3):
                if a != i + 1:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
        return min(dp)
"""        
    
    
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
        
            