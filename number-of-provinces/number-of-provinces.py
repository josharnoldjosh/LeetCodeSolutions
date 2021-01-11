class DSU:
    
    def __init__(self, N):
        self.p = list(range(N))
    
    def find(self, x):
        if self.p[x] == x:
            return x
        return self.find(self.p[x])
    
    def union(self, x, y):
        if self.p[x] != self.p[y]:            
            self.p[self.find(x)] = self.find(y)
​
​
class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        N = len(isConnected)
        dsu = DSU(N)
                        
        for i in range(N):
            for j in range(N):
                if isConnected[i][j] == 1:
                    dsu.union(i, j)
                    
        return len(set(dsu.find(i) for i in range(N)))
