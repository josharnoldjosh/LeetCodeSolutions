class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @functools.lru_cache(maxsize=None)
        def recurse(p1, p2):
            if p1 == len(text1): return 0
            if p2 == len(text2): return 0
            score = 0
            if text1[p1] == text2[p2]:
                score = max(score, recurse(p1+1, p2+1) + 1)
            else:
                score = max(recurse(p1+1, p2), recurse(p1, p2+1))
            return score
        
        return recurse(0, 0)