class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = collections.Counter(s)
        
        for idx, c in enumerate(s):
            if counts[c] == 1:
                return idx
            
        return -1
    
​
