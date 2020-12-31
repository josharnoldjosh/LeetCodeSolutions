class Solution:
    def isValid(self, s: str) -> bool:
        
        stack, mapping = [], {')':'(', ']':'[', "}":'{'}
        
        for c in s:
            if c in {'(', '{', '['}:
                stack.append(c)
            elif len(stack) > 0 and mapping[c] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return stack == []
            
