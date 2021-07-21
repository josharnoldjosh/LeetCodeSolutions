class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        uf = {i: i for i in range(n)}
        self.groups = n
        
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def merge(i, j):
            i, j = find(i), find(j)
            if i != j:
                self.groups -= 1
                uf[i] = j
                
        for t, i, j in sorted(logs):
            merge(i, j)
            if self.groups == 1:
                return t
            
        return -1
            