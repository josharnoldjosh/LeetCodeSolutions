class Solution:
    def decodeString(self, s: str) -> str:
        
        stack, tmp_num = [[1, ""]], ""
                 
        for c in s:            
            if c.isnumeric():
                tmp_num += c                
            elif c == "[":
                stack.append([int(tmp_num), ""])
                tmp_num = ""                
            elif c == "]":
                num, text = stack.pop()
                stack[-1][-1] += num*text
            else:
                stack[-1][-1] += c
                
        return stack[-1][-1]