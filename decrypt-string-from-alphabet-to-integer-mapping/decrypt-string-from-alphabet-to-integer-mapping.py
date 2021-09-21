class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        d = {str(i): chr(ord('a') + i - 1) 
             for i in range(1, 27)}
        
        stack = list(s)
        result = []
        
        while stack:
            i = stack.pop()
            if i != '#':
                result.append(d[i])
                continue
            tmp = stack.pop() + stack.pop()
            result += d[tmp[::-1]]
            
        return "".join(result[::-1])
        