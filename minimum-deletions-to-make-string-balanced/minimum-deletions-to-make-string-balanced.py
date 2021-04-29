class Solution:
    def minimumDeletions(self, s: str) -> int:
                        
        a_idx = [0] + list(itertools.accumulate([1 if c == 'a' else 0 for c in s]))
        b_idx = [0] + list(itertools.accumulate([1 if c == 'b' else 0 for c in s]))
        
        result = float('inf')
        
        for idx in range(len(s)):
            result = min(
                result,
                a_idx[-1] - a_idx[idx+1] +  b_idx[idx] - b_idx[0]
            )
        
        return result
        

    
"""

Recursive Idea: Unfortunately it TLE's.

```python
class Solution:
    def minimumDeletions(self, s: str) -> int:

        def recurse(i, j):            
            if i == len(s): return 0
            return recurse(i+1, j) + (s[i] == ('b' if i <= j else 'a'))
             
        return min([recurse(0, j) for j in range(-1, len(s)+1)])
```
"""

