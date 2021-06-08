class Solution:
    def checkValidString(self, s: str) -> bool:
        
        lo = hi = 0
        
        for c in s:
            lo += (1 if c == '(' else -1)
            hi += (1 if c != ')' else -1)
            if hi < 0: break
            lo = max(lo, 0)
            
        return lo == 0
    
    
"""
I wish this worked, but TLE:

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        
        def push(idx):
            stack.append('(')
            if backtrack(idx+1):
                return True
            stack.pop()
            
        def pop(idx):
            try: stack.pop()
            except: return False
            if backtrack(idx+1):
                return True
            stack.append('(')
            return False
        
        def backtrack(idx):
            
            if idx >= len(s): return not stack
            
            c = s[idx]
            
            if c == '(':
                if push(idx): return True                
            elif c == ')':
                if pop(idx): return True                
            elif c == '*':                
                if backtrack(idx+1): return True                
                if push(idx): return True
                if pop(idx): return True
                                            
        return backtrack(0)
```

This one is even cleaner but still TLE:

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        def recurse(idx, stack):            
            if idx >= len(s): return not stack
            c = s[idx]
            if c == '(':
                return recurse(idx+1, stack+[c])
            elif c == ')':
                return recurse(idx+1, stack[:-1]) if stack else False
            return any([
                recurse(idx+1, stack),
                recurse(idx+1, stack+[c]),
                recurse(idx+1, stack[:-1]) if stack else False
            ])

        return recurse(0, [])
```
"""
                
        
        
        
        