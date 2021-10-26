class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def process(x):
            stack = []
            for c in x:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack += [c]
            return ''.join(stack)
        
        return process(s) == process(t)
                
        
        