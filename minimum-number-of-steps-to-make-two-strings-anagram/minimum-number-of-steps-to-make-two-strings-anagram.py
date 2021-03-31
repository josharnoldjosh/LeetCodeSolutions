from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s, t = Counter(s), Counter(t)
        result = (s | t) - (s & t)
        return sum(result.values()) // 2
    
"""
- Counter for s 
- Counter for t 


"""