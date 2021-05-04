from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def isPossible(self, nums: List[int]) -> bool:        
        
        heaps = defaultdict(list)
        
        for i in nums:
            if heaps[i-1]:
                heappush(heaps[i], heappop(heaps[i-1]) + 1)
            else:
                heappush(heaps[i], 1)
                
        return all(
            count >= 3
            for counts in heaps.values()            
            for count in counts
        )