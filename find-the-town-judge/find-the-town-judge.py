class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:        
        
        counts = collections.Counter()
        for a, b in trust:
            counts[b] += 1
            
        cannidates = set(range(1, n+1)) - set([i[0] for i in trust])
        
        for i in cannidates:
            if counts[i] == n-1:
                return i
        
        return -1 
            
        
    
"""

"""