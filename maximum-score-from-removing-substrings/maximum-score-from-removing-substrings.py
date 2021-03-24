class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        # First, we always make 'x' > 'y'
        a, b = 'a', 'b'
        if x < y:
            x, y = y, x
            a, b = b, a
            
        # Define our variables
        seen = collections.Counter()
        result = 0
        
        # For each character in s
        for c in s+'#':
                        
            # Try to pop 'ab' when c is in "ab"
            if c in "ab":                                
                if c == b and seen[a] > 0:
                    result += x
                    seen[a] -= 1
                else:
                    seen[c] += 1                
                continue

            # Try to pop "ba" when c != 'ab'
            result += y * min(seen[a], seen[b])
            seen = collections.Counter()
        
        return result
    
"""
      a = 'a'
        b = 'b'
        if x < y:
            x, y = y, x
            a, b = b, a
        seen = Counter()
        ans = 0
        for c in s + 'x':
            if c in 'ab':
                if c == b and 0 < seen[a]:
                    ans += x
                    seen[a] -= 1
                else:
                    seen[c] += 1
            else:
                ans += y * min(seen[a], seen[b])
                seen = Counter()

        return ans
"""