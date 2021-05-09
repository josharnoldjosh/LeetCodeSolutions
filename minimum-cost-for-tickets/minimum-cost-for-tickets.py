class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        days = set(days)
        dp = [1 if i in days else 0 for i in range(1, max(days)+1)]
        graph = {0 : 1, 1 : 7, 2: 30}
        
        @functools.lru_cache(None)
        def recurse(day):
            
            if day >= len(dp):
                return 0
            
            if dp[day] == 0:
                return recurse(day+1)
            
            return min([
                c + recurse(day+graph[i])
                for i,c in enumerate(costs)   
            ])
        
        return recurse(0)
    
    

    
"""
minimum cost

- choosing either a 1, 7 or 30 day pass, and jumping ahead accordingly
"""