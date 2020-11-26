from functools import lru_cache
​
​
class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:                        
        return self.recurse(m-1, n-1)
                    
    @lru_cache(maxsize=None)
    def recurse(self, m, n):
        if m < 0 or n < 0: return 0
        if m == 0 and n == 0: return 1
        return self.recurse(m-1, n) + self.recurse(m, n-1)
