class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
                                    
        if not nums:
            return 0
        
        @functools.lru_cache(maxsize=None)
        def dfs(node):
            if graph[node] in graph:
                return 1 + dfs(graph[node])
            return 1
            
        graph = collections.defaultdict(list)
          
        for i in nums:            
            graph[i] = i+1
                        
        return max(
            dfs(i)
            for i in graph.keys()
        )
            
            
                

"""
1->?
2->?

"""