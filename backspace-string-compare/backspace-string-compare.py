from functools import reduce


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def operation(s, c):
            if c == '#':
                return s[:-1]
            else:
                return s + c
            
        return reduce(operation, s, "") == reduce(operation, t, "")
        
        