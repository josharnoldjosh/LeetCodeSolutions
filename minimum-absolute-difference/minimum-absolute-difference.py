class Solution:
    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
        A.sort()

        res = collections.defaultdict(list)

        for a, b in zip(A, A[1:]):
            if res and b - a > min(res.keys()):
                continue
            res[b - a].append((a, b))            

        return res[min(res.keys())]
                
        
"""

Brute force: TLE

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        results = []
        for idx, i in enumerate(arr):
            for jdx, j in enumerate(arr):
                if idx == jdx: continue
                if i >= j: continue
                results += [
                    (i, j, j-i)
                ]
                
        key = min(results, key=lambda x: x[-1])[-1]
                                
        return list(sorted([[a, b] for (a, b, c) in results if c == key]))
                
```
"""