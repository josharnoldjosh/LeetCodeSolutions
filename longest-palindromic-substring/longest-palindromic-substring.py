class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        @functools.lru_cache(maxsize=None)
        def expandFromCenter(i, j):
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i -= 1; j += 1
            return s[i+1:j]
                
        result = []
        result += [expandFromCenter(i, i) for i in range(len(s))]
        result += [expandFromCenter(i, i+1) for i in range(len(s)-1)]
        return max(result, key=len)
            
            
            
            
