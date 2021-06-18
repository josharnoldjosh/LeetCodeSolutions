from heapq import *


class Solution:
    
    def findContentChildren(self, g, s, score = 0):
                        
        heapify(s)
        
        for factor in sorted(g):
            
            if not s:
                break
                                            
            x = -1
            
            while x < factor and s:
                x = heappop(s)
                                    
            if x >= factor:
                score += 1
                
        return score
        