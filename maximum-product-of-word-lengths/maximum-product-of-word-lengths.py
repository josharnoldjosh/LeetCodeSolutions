class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = [(set(i), len(i)) for i in words]
        
        result = 0
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j: continue
                if words[i][0] & words[j][0]: continue
                result = max(result, words[i][1]*words[j][1])
        
        return result
    
"""
- intersection of strings many times
- O(n^2) algorithm...
- only interested in set right? (besides length)
"""