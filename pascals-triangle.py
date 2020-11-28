from functools import lru_cache
​
​
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
                
        @lru_cache(maxsize=None)
        def row(n):        
            if n == 1: return [1]
            if n == 2: return [1, 1]        
            result = [1]                    
            for i in range(n-2):
                result.append(sum(row(n - 1)[0+i:2+i]))                              
            result += [1]            
            return result
                                    
        return [row(i) for i in range(1, numRows+1)]
    
    
