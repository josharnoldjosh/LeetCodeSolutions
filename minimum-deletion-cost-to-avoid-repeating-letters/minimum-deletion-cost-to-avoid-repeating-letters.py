class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:        
        

        last_char = ''
        heap = []
        result = 0
        
        for i, c in enumerate(s):            
            if c != last_char and len(heap) <= 1:
                heap = [cost[i]]
                last_char = c                
            elif c != last_char and len(heap) >= 2:                
                while len(heap) > 1:                    
                    result += heapq.heappop(heap)                    
                last_char = c
                heap = [cost[i]]
            else:
                heapq.heappush(heap, cost[i])
                    
        while len(heap) > 1:            
            result += heapq.heappop(heap)
            
                    
        return result