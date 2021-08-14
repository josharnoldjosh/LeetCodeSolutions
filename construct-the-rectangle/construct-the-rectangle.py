class Solution:
    def constructRectangle(self, area: int) -> List[int]:
    
        mid = int(area ** 0.5)
        
        while mid > 0:
            if area % mid == 0:
                return [area // mid, mid]
            mid -= 1
        return [area, 1]