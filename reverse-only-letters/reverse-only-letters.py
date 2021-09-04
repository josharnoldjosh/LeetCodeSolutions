class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        stack = []
        
        for c in s:
            if c.isalpha():
                stack += [c]
                
        return "".join([
            c 
            if not c.isalpha()
            else stack.pop()
            for idx, c in enumerate(s)
        ])