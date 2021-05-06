class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        delete = set()
        stack = []
        
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if s[i] == "(":
                stack.append(i)
            elif not stack:
                delete.add(i)
            else:
                stack.pop()
                
        delete = delete.union(set(stack))
        return "".join(c for i, c in enumerate(s) if i not in delete)
                    
                
    
    
"""
First thoughts:
- One source of information is the "count"
- There should be an event count...

- Also direction:
    - ))((
    

((((())))


"""

