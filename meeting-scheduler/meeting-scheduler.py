from heapq import *


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        heap = [x for x in slots1 + slots2 if x[1]-x[0] >= duration]
        heapify(heap)
        
        while len(heap) > 1:
            x, y = heappop(heap), heappop(heap)
            
            if x[1] > y[0] and abs(max(x[0], y[0]) - min(x[-1], y[-1])) >= duration:
                print(x, y)
                res = max(x[0], y[0])
                return [res, res+duration]
            
            heappush(heap, y)
            continue
            
        return []
            
            
        
"""
          1
**********
    ***********

"""