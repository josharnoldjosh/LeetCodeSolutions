class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        stack = []
        for c in S:
            if c == "(":
                stack.append(c)
                if len(stack) > 1:
                    result += "("
            else:
                stack.pop()
                if len(stack) >= 1:
                    result += ")"        
        return result