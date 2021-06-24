class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        result, end = 0, float('inf')
        
        for i, j in sorted(points, reverse=True):
            if end > j:
                result += 1
                end = i
            
        return result
        
        
"""
      ret, shoot = 0, float('inf')
        for s, e in sorted(points, reverse=True):
            if shoot > e:
                shoot = s
                ret += 1
        return ret
"""