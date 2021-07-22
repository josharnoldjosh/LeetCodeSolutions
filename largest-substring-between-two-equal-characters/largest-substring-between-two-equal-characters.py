class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        counts = collections.Counter(s)
        s_prime = s[::-1]
        result = 0
        
        if counts.most_common(1) and counts.most_common(1)[0][1] < 2:
            return -1
        
        for k, v in [i for i in counts.items() if i[1] >= 2]:
            i, j = s.index(k), len(s) - s_prime.index(k) - 1            
            result = max(result, j-i-1)
        
        return result
    
"""
we don't care what's in between them
"""