class Solution:
    def stoneGame(self, piles: List[int]) -> bool:        
        
        @functools.lru_cache(None)
        def recurse(stones):
            if len(stones) == 0: return 0
            x = stones[0] - recurse(stones[1:])
            y = stones[-1] - recurse(stones[:-1])
            return max(x, y)
        
        return True if recurse(tuple(piles)) > 0 else False
