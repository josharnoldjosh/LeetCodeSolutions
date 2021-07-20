class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = {}
        for (src, dst) in paths:            
            graph[src] = dst            
        return list(set([j for i in paths for j in i]) - set(graph.keys()))[0]