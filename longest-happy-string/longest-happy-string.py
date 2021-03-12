class Solution:
    
    def longestDiverseString(self, a: int, b: int, c: int) -> str:                
        
        result = ""        
        
        heap = list(zip((-a,-b,-c), ('a','b','c')))
        heapq.heapify(heap)                  
        
        prev_val = 0
        prev_char = ''
        
        while heap:
                                      
            v, k = heapq.heappop(heap)
            
            if prev_val < 0:
                heapq.heappush(heap, (prev_val, prev_char))
                
            if abs(v) >= 2 and abs(v) > abs(prev_val):
                result += k*2
                v += 2
            elif abs(v) >= 1:
                result += k
                v += 1
            else:
                break
                
            prev_val = v
            prev_char = k
                
                                                                     
        return result
                
            

        
        
"""

keep adding max until can't add max


ccaccbcc
"""