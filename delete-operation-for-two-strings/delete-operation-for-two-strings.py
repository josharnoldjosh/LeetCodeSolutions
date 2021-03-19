class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @functools.lru_cache(None)
        def recurse(i, j):
            x, y = word1[i:i+1], word2[j:j+1]
            if x == y == "": return 0
            if x == "" or y == "": return max(len(word1[i:]), len(word2[j:]))
            if x == y: return recurse(i+1, j+1)
            return 1 + min(recurse(i+1, j), recurse(i, j+1))
        
        return recurse(0, 0)