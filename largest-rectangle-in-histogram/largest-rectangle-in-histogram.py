class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        result, stack = 0, []
                                            
        for idx, i in enumerate(heights+[0]):

            while stack and heights[stack[-1]] > i:
                h = heights[stack.pop()]
                w = idx - stack[-1] - 1 if stack else idx                                                        
                result = max(result, w * h)                        
                
            stack.append(idx)
                
        return result