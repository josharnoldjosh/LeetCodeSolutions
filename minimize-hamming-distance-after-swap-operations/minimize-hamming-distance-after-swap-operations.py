class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        
    def find(self, x):
        if self.p[x] == x: return x
        return self.find(self.p[x])
    
    def union(self, a, b):
        if self.p[a] != self.p[b]:
            self.p[self.find(a)] = self.find(b)
​
​
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        N = len(source)
        uf = UnionFind(N)
        graph = collections.defaultdict(set)
        result = 0
        
        # Build connected components of indexes
        for i, j in allowedSwaps:
            uf.union(i, j)
                       
        # Map parent to its indexes
        for i in range(N):
            graph[uf.find(i)].add(i)
            
        # For each "parent", compare what indexes we have
        # Subtract the difference in counts
        # What we have left is the indexes that we couldn't swap
        for idx in graph.values():
            A = [source[i] for i in idx]
            B = [target[i] for i in idx]            
            result += sum((collections.Counter(A) - collections.Counter(B)).values())
            
