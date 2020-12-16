class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @functools.lru_cache(None)
        def recurse(i):
            if i == 0: return False
            for j in range(1, int(i**0.5)+1):
                if not recurse(i - j*j):
                    return True
            return False
        
        return recurse(n)
