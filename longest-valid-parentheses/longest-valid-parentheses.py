class Solution:
    def longestValidParentheses(self, s: str) -> int:
                
        result = 0
        stack = [(-1, ')')]
        
        for idx, i in enumerate(s):
            if i == ')' and stack[-1][-1] == '(':
                stack.pop()
                result = max(result, idx - stack[-1][0])
            else:
                stack += (idx, i),
            
        return result
