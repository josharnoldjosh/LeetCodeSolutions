class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        result = float('inf')
        
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    result = min(result, (area if area > 0 else float('inf')))
            seen.add((x1, y1))
            
        return result if result < float('inf') else 0
    
    
"""
    def minAreaRect(self, points):
        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < res:
                        res = area
            seen.add((x1, y1))
        return res if res < float('inf') else 0
"""