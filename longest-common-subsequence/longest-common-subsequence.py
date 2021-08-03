class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:        
            
        @lru_cache(maxsize=None)
        def recurse(idx, jdx):
            if idx == len(text1) or jdx == len(text2):
                return 0
            a, b = recurse(idx+1, jdx), 0
            occ = text2.find(text1[idx], jdx)
            if occ != -1:
                b = 1 + recurse(idx+1, occ+1)
            return max(a, b)
        
        return recurse(0, 0)
            

        
    
    
"""
- what if we found the LCS of size one
- then from LCS of 1, we use that as a building block for LCS of size 2?
"""