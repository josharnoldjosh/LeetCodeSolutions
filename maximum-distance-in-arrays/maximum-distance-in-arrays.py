class Solution:
    
    def maxDistance(self, arrays: List[List[int]]) -> int:        
        
        if not arrays: return 0        
        
        min_idx = arrays.index(min(arrays, key = lambda x: x[0]))
        max_idx = arrays.index(max(arrays, key = lambda x: x[-1]))
        
        result = 0
        
        for idx, a in enumerate(arrays):
            result = max(
                result,
                abs(arrays[min_idx][0] - a[-1]) if idx != min_idx else 0,
                abs(arrays[max_idx][-1] - a[0]) if idx != max_idx else 0,
            )
            
        return result
            
                
                
            
    
    
"""
How do you make sure, the min and max are not from the same window 


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = 0
        
        for idx, i in enumerate(arrays):
            for jdx, j in enumerate(arrays):
                if idx == jdx: continue
                result = max(
                    result,
                    abs(i[0]-j[-1]),
                    abs(j[0]-i[-1]),
                )
        
        return result
"""
