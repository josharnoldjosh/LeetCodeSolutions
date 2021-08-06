class Solution:
    def reverseParentheses(self, s: str) -> str:
        result = ""
        stack = []
        for c in s:
            if c == "(":
                stack += [""]
            elif c == ")":                                
                temp = "".join(stack.pop())[::-1]
                if stack:
                    stack[-1] += temp
                else:
                    result += temp
            elif stack:
                stack[-1] += c      
            else:
                result += c
                    
        return result