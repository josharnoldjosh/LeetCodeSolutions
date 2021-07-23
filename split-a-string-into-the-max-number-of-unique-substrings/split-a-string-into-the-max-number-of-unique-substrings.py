class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        global score
        score = 0
        
        def recurse(s, seen):
            global score
            
            # Base case
            if not s:
                score = max(
                    score,
                    len(seen - {''})
                )
            
            # 1)
            if s not in seen:
                recurse("", seen | {s})
                
            # 2) 
            for i in range(1, len(s)):
                if s[:i] not in seen:
                    recurse(s[i:], seen | {s[:i]})
            
            
        recurse(s, set())
        return score
            
            
        
    
    
"""
a b a b a

""" 