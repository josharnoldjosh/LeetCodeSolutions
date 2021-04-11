class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @functools.lru_cache(None)
        def recurse(i, j):
            if i >= len(triangle): return 0 # we've reached bottom so okay to terminate successfully
            row = triangle[i]
            if j >= len(row): return -float('inf') # we may not have reached bottom yet
            return row[j] + min(
                recurse(i+1, j),
                recurse(i+1, j+1)
            )
        
        return recurse(0, 0)
            
            
    
"""
Greedy clearly wouldn't work.

Need to try all examples...


"""

