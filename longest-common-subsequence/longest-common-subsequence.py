class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @functools.lru_cache(maxsize=None)
        def recurse(idx, jdx):
            
            if (
                idx == len(text1)
                or jdx == len(text2)           
            ):
                return 0
            
            option_a = recurse(idx+1, jdx)
            
            option_b = 0            
            occurance = text2.find(text1[idx], jdx)
            if occurance != -1:
                option_b = 1 + recurse(idx+1, occurance+1)
                
            return max(
                option_a,
                option_b
            )
        
        return recurse(0, 0)