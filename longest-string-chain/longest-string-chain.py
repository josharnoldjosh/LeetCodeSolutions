from collections import (
    defaultdict,
    Counter
)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:        
        
        words = set(words)
        
        @functools.cache
        def recurse(word):
            if word not in words: return 0
            result = max([1 + recurse(word[:i] + word[i+1:]) for i in range(len(word))])
            return result if result else 0
        
        return max([0]+[
            recurse(word)
            for word in words
        ])
                
        