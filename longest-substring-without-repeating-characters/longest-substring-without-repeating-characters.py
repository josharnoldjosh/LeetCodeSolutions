class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        
        i, j = 0, 1
        
        result = 0
        
        s = s.replace(" ", "Œ")
        
        while j <= len(s)+1:                               
            count = collections.Counter(s[i:j]).most_common(1)                        
            if not count:
                j += 1
                i = j-1            
                result = max(result, len(s[i:j]))
            elif count[0][-1] <= 1:
                result = max(result, len(s[i:j]))
                j += 1
            else:                
                i += 1
                
        return result
    
"""
T(n) = 2 * T(n - 1) -> 2^n
"""