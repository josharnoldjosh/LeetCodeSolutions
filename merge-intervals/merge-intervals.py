class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x)
        
        result = []
        
        for start, end in intervals:
            
            if result == []:
                result.append([start, end])
                continue
                
            if start > result[-1][-1]:
                result.append([start, end])
                continue
                
            if end > result[-1][-1] and start > result[-1][0]:
                result[-1][-1] = end
                continue
                
            if start <= result[-1][0] and result[-1][-1] <= end:
                result[-1] = [start, end]
                continue
                                                      
        return result
        
    
​
"""
Case:
​
X00
XXX00
XXXXX00
XXXXXXX00
0000000000
                 
"""
