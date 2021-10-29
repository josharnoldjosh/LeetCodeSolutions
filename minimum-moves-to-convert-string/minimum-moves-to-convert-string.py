class Solution:
    def minimumMoves(self, s: str) -> int:
        
        # Pad "s"
        s += "OOO"
        
        i, result = 0, 0
                
        while i < len(s)-3:
            window = s[i:i+3]
            if window in ["XOX", "XXX", "XOO", "XXO"]:
                i += 3
                result += 1
            else:
                i += 1
                
        return result