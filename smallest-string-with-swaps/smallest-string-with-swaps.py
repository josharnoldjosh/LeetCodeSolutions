class UnionFind:
    
    def __init__(self, n):
        self.p = list(range(n))
        
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
    
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
                
        uf = UnionFind(len(s))
        
        result, graph = [], collections.defaultdict(list)
        
        for a, b in pairs:
            uf.union(a, b)
            
        for idx, c in enumerate(s):
            graph[uf.find(idx)].append(c)
            
        for key in graph.keys():
            graph[key].sort(reverse=True)
            
        for idx in range(len(s)):
            result.append(graph[uf.find(idx)].pop())
            
        return "".join(result)
            
        
        
