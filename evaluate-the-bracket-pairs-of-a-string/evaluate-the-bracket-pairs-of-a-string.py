class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
                
        graph = {x[0] : x[1] for x in knowledge}        
        stack = []
        result = ""
        
        for c in s:
            if c not in '()':
                if not stack: result += c
                else: stack.append(c)
            elif c == '(':
                stack.append('(')
            elif c == ')':
                key = ''.join(stack)[1:]
                result += graph[key] if key in graph else "?"
                stack.clear()
                
        return result
                
                    
            
        
     
    
    
"""
List[List[str]] -> {str : str}

xxx(
hello) 
xxx(world
xxxx
"""