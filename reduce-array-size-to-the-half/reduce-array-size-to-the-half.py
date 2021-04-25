class Solution:
    def minSetSize(self, arr: List[int]) -> int:        
        counts = collections.Counter(arr).most_common()
        result = 0
        remaining = len(arr) / 2
        while remaining > 0:
            remaining -= counts.pop(0)[1]
            result += 1        
        return result
        
    
"""
at least half

1. could we count? 
2. Choose a greedy approach?
"""