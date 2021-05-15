from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        
        result = 0
        left, right = Counter(), Counter(s)
        
        for c in s:
            left[c] += 1
            right[c] -= 1
            if not right[c]:
                del right[c]
            if len(left) == len(right):
                result += 1
        
        return result
    
    
"""
Brute Force:

```python
class Solution:
    def numSplits(self, s: str) -> int:
        
        result, key = 0, set(s)
        
        for idx in range(1, len(s)):
            a = len(set(s[:idx]) & key)
            b = len(set(s[idx:]) & key)
            if a == b: result += 1
                
        return result
```
"""