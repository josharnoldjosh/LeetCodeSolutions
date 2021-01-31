class Solution:
    def restoreArray(self, A: List[List[int]]) -> List[int]:
                                
        graph = collections.defaultdict(list)
        for i, j in A:
            graph[i].append(j)
            graph[j].append(i)
                    
        
        start = None
        for i in graph.keys():
            if len(graph[i]) == 1:
                start = i
                
        result, seen = [], set()
                
        def dfs(i):
            seen.add(i)
            for next_node in graph[i]:
                if next_node not in seen:
                    dfs(next_node)
            result.append(i)
            
        dfs(start)
            
        return result
        
        
            
            