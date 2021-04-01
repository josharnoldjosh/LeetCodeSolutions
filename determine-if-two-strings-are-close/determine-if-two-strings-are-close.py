from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a, b = Counter(word1), Counter(word2)        
        if set(a.keys()) != set(b.keys()): return False
        if sorted(a.values()) != sorted(b.values()): return False
        return True
    
"""
- Swap any two existing characters (in same string?)
- Turn all X's in Y's and Y's into X's, where X and Y are characters and X != Y
- Its a boolean return: not a min or max etc

bac
abc

- If we can swap, order doesn't matter, right, so just character count?
- If we have a dictionary of counts, it doesn't matter which char maps to which count
    - only that the exact number of counts are the same 
    - and that the chars are there 
    
- check the keys are the same...
- check the values are the same...?
"""