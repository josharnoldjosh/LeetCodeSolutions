import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        result, min_heap = [], []
        
        for i in nums1:
            for j in nums2:
                heapq.heappush(min_heap, (i+j, i, j))
                               
        print(min_heap)
                    
        for _ in range(k):
            if not min_heap: break
            result.append(heapq.heappop(min_heap)[1:])            
            
        return result