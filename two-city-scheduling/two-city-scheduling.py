class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        @functools.cache
        def recurse(idx, a, b):
            if idx >= len(costs): return 0 if a == b else float('inf')
            return min(
                costs[idx][0] + recurse(idx+1, a+1, b),
                costs[idx][1] + recurse(idx+1, a, b+1),
            )
        
        return recurse(0, 0, 0)