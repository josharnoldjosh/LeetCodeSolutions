class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        graph = collections.defaultdict(list)
        
        for idx, c in enumerate(S):
            graph[c].append(idx)
            
        intervals = [[x[0], x[-1]] for x in graph.values()]
        
        # intervals.sort(key=lambda x: x[0])
        
        merged_intervals = []
        
        for a, b in intervals:                                    
            if merged_intervals == []:
                merged_intervals.append([a, b])                                    
            elif merged_intervals[-1][-1] > a:
                merged_intervals[-1][-1] = max(merged_intervals[-1][-1], b)                
            elif merged_intervals[-1][-1] > b:
                continue                
            elif merged_intervals[-1][-1] < a:
                merged_intervals.append([a, b])
                        
            
        return [x[-1]-x[0]+1 for x in merged_intervals]