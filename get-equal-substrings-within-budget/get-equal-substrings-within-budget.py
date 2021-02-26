class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        window = collections.deque([])
        best = 0
        i = 0
        
        while i < len(s):
            
            cost = abs(ord(s[i]) - ord(t[i]))
            
            if maxCost - cost >= 0:
                window.append(cost)
                maxCost -= cost
                best = max(best, len(window))
                i += 1
                continue
            
            if len(window) > 0:
                maxCost += window.popleft()
                continue
                
            i += 1
                
        return best
              
                
            

  