class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = list(zip((-a, -b, -c), tuple("abc")))
        heapq.heapify(heap)
        
        result = ""
        
        prev_num, prev_char = 0, ''
        
        while heap:            
            
            num, char = heapq.heappop(heap)
            
            if abs(num) >= 2 and abs(num) > abs(prev_num):
                result += char*2
                num += 2
            elif abs(num) >= 1:
                result += char
                num += 1
            else:
                break
                
            if abs(prev_num) > 0:
                heapq.heappush(heap, (prev_num, prev_char))
                
            prev_num, prev_char = num, char
            
        
        return result
                
            
        
        
        
    
    
"""

3, 3, 3

aababbccc X

1 1 1

aabbccabc

10, 2, 2

aabaabaacaacaa

if previous is greater than current...?





"""
        