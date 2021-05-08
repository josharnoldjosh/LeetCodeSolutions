class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height)-1
        
        result = 0
        
        while l < r:            
            result = max(result,  min(height[l], height[r]) * (r-l))            
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return result
    
    
"""
Area := W * H

We are controlling the width and height.

Width is guarunteed to decrease each time.

Always select whatever increases height?
"""