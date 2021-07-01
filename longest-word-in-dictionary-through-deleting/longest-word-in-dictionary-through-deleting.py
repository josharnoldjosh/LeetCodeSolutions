class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
                
        words = [collections.deque(word) for word in dictionary]
        
        results = set()
        
        for c in s:
            for idx in range(len(words)):
                if words[idx] and c == words[idx][0]:
                    words[idx].popleft()
                if not words[idx]:
                    results.add(dictionary[idx])
                    
        results = list(results)
        results.sort(reverse=True)
        results.sort(key=len)                        
        
        return "" if not results else results[-1]
        
        
"""

Counter intersection! Fast... but need order


A brute force attempt! Clean code, but TLE!

```python
def findLongestWord(s, dictionary):

    results = collections.defaultdict(list)

    def dfs(idx, i):
        if i in dictionary: results[len(i)].append(i)
        if idx >= len(s): return            
        dfs(idx+1, i)
        dfs(idx+1, i+s[idx])

    dfs(0, "")

    return list(sorted(results[max(results.keys())]))[0]            
```

"""