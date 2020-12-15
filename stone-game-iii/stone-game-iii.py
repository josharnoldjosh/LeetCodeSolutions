class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @functools.lru_cache(maxsize=None)
        def dp(idx):
            if idx >= len(stoneValue): return 0            
            return max([sum(stoneValue[idx:jdx]) - dp(jdx) for jdx in range(idx+1, idx+4)])        
                
        score = dp(0)
                                        
        if score > 0: return "Alice"
        if score < 0: return "Bob"
        return "Tie"
