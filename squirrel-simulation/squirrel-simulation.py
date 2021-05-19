class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
                        
        distance = lambda i, j: abs(i[0]-j[0]) + abs(i[1]-j[1])        
        result = 0
        d = -float('inf')
        
        for nut in nuts:
            result += distance(nut, tree) * 2
            d = max(d, distance(nut, tree) - distance(nut, squirrel))
            
        return result - d
       
        
        
        

    
    
"""
Greedy Idea

```python

```


Backtracking Idea (TLE)

```python
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
                        
        seen, nuts = set(), [tuple(i) for i in nuts]
                
        def score(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
                        
        def backtrack(x, y):   
            
            if len(seen) == len(nuts):
                return score((x, y), tree)
            
            best = float('inf')
            
            for nut in nuts:
                if nut in seen: continue                    
                seen.add(nut)
                res = score((x, y), nut) + backtrack(*nut)                
                best = min(res, best)
                seen.remove(nut)
                                
            return best
        
        return backtrack(*squirrel)
```
"""