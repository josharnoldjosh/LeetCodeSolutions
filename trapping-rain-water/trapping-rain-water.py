class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = []
        result = 0
        
        for idx, i in enumerate(height):            
            while stack and height[stack[-1]] < i:
                lower = height[stack.pop()]
                if not stack: break
                upper = min(height[stack[-1]], i)
                h = upper - lower
                w = idx - stack[-1] - 1
                result += w * h
                                        
            stack.append(idx)
        
        return result