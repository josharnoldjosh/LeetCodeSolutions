class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        graph = collections.defaultdict(collections.deque)
        
        for idx, i in enumerate(groupSizes):
            graph[i].append(idx)
            
        result = []
        
        for key, val in graph.items():
            while val:
                tmp = []
                for i in range(key):
                    tmp += [val.popleft()]
                result.append(tmp)                
        
        return result
        
    
"""
Two hard things:
- 1. we can have an entire group of size three's
    - even if we group threes togethers, we have to "sub group them?
    
group size -> people
sliding window into results
"""