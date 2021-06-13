class Solution:
    def maxScore(self, A: List[int], k: int) -> int:            
        prefix_sum, window_size = [0] + list(itertools.accumulate(A)), len(A) - k
                                                     
        return max([
            prefix_sum[-1] - (prefix_sum[i+window_size] - prefix_sum[i])
            for i in range(len(A)-window_size+1)
        ])        
    
    
"""
Top Down [TLE]

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        @functools.cache
        def recurse(l, r, k):
            if k == 0: return 0
            return max(
                cardPoints[l] + recurse(l+1, r, k-1),
                cardPoints[r] + recurse(l, r-1, k-1),
            )
        
        return recurse(0, len(cardPoints)-1, k)
```

One liner (expanded out for readability) [TLE]

```python
return sum(A) - min([
    sum(A[i:i+len(A)-k])
    for i in range(len(A))
    if i+len(A)-k <= len(A)
])
```
"""