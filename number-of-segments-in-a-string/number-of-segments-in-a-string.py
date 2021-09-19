class Solution:
    def countSegments(self, s: str) -> int:
        
        result, stack = 0, []
        
        for c in s:
            if c == ' ':
                if stack:
                    result += 1
                stack.clear()
            else:
                stack += [c]
                
        return result + (1 if stack else 0)