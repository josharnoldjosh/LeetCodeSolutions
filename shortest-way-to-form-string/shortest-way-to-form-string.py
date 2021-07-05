class Solution:
    def shortestWay(self, source: str, target: str) -> int:        
        
        
        @functools.lru_cache(None)
        def is_subsequence(x):
            it = iter(source)
            return all(c in it for c in x)
        
        
        queue = collections.deque(target)
        temp = ""
        result = 1
        
        while queue:
            temp += queue[0]
            if is_subsequence(temp):
                queue.popleft()
                continue
            if not is_subsequence(queue[0]):
                return -1
            temp = queue.popleft()
            result += 1
                
        return result
        
        
        
        
        
        
"""

Divide & Conquer idea. This times out :( but I thought it would be cool to write in an interview!

```python
class Solution:
    def shortestWay(self, source: str, target: str) -> int:        
        
        @functools.lru_cache(None)
        def is_subsequence(x):
            it = iter(source)
            return all(c in it for c in x)
        
        @functools.lru_cache(None)
        def divide_and_conquer(x):
            if not x: return 0
            if is_subsequence(x): return 1
            return min([
                divide_and_conquer(x[:i]) + divide_and_conquer(x[i:])
                for i in range(1, len(x))
            ] + [float('inf')])
        
        result = divide_and_conquer(target)
        
        return result if result != float('inf') else -1
```
"""