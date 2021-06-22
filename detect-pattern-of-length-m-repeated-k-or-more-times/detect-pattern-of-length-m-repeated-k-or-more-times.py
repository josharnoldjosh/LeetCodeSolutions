class Solution:        
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:                        
        
        def contains_pattern(x):
            counts = collections.Counter()
            for i in range(0, len(x), m):
                counts[tuple(x[i:i+m])] += 1
            return counts.most_common(1)[0][1] >= k
        
        window_size = m * k
        
        for i in range(len(arr)-window_size+1):            
            if contains_pattern(arr[i:i+window_size]):
                return True
            
        return False
        
    
"""
1. get cannidates 
2. see if you can find cannidates that don't overlap greater than k
"""