class Solution:
    def maxArea(self, height: List[int]) -> int:
                
        p1, p2, result = 0, len(height)-1, 0
        
        while p1 != p2:
            
            score = min(height[p1], height[p2]) * (p2 - p1)
            
            result = max(result, score)
                                    
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
                            
        return result
