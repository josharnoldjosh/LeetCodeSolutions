class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []        
        for i in range(1, (n // 2)+1):
            result += [i, -i]
        if len(result) < n: result += [0]
        return result
    
"""
- array will be of length n
- integers must be "unique"
"""