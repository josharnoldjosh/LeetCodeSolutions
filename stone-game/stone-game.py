class Solution:
    def stoneGame(self, piles: List[int]) -> bool:        
        
        @functools.lru_cache(maxsize=None)
        def recurse(i, j):
            if i > j: return 0
            return max(
                piles[i] - recurse(i+1, j),
                piles[j] - recurse(i, j-1),
            )
        
        return True if recurse(0, len(piles)-1) >= 0 else 0