class Solution:
    def maxDepth(self, s: str) -> int:
        stack, res = [], 0    
        for c in s:
            if c not in "()": continue
            if c == "(":
                stack.append(c)
                res = max(res, len(stack))
            else:
                stack.pop()
        return res