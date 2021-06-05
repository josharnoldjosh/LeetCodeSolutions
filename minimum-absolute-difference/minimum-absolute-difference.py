class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        
        data = list(zip(arr, arr[1:]))
        
        res = collections.defaultdict(list)
        for i in data:
            res[i[1]-i[0]].append(i)
        
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