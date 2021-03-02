class Solution:
    def numSub(self, s: str) -> int:        
        result = 0        
        for x in s.split('0'):            
            if not x: continue
            result += sum([i+1 for i in range(len(x))])
        return result % ((10 ** 9) + 7)
    
"""
x, y
1, 1
2, 3
3, 6
4, 10
5, 15
6, 21
7, 28
8, 36
"""