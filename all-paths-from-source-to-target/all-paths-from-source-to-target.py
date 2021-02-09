class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs_with_backtracking(node, path):
            seen.add(node)
            
            if node == target:
                result.add(tuple(path))
                return
            
            for next_node in mapping[node]:
                if next_node in seen: continue
                seen.add(next_node)
                dfs_with_backtracking(next_node, path+[next_node])
                seen.remove(next_node)
                
            return
                        
        mapping = collections.defaultdict(list)
        
        for idx, i in enumerate(graph):            
            mapping[idx].extend(i)
            
        seen = set()
        result = set()
        target = len(graph)-1
                
        dfs_with_backtracking(0, [0])
        
        return list(result)