class DSU:
    def __init__(self):
        self.parent = list(range(1001))
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        if self.parent[self.find(x)] == self.find(y):
            return False
        self.parent[self.find(x)] = self.find(y)
        return True
​
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for i in edges:
            if not dsu.union(*i):
                return i
        raise Exception("Uh Oh")
