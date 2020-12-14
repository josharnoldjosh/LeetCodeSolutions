class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        # Prefix array
        for i in range(len(piles) - 2, -1, -1):
            piles[i] += piles[i+1]
            
        @functools.lru_cache(None)
        def dp(i, m):
            if i + (2*m) >= len(piles): return piles[i]
            return piles[i] - min(
                dp(
                    i+x, 
                    max(m, x)
                ) for x in range(1, (2*m) + 1)
            )
        
        return dp(0, 1)
