class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        if not heights:
            return 0
        
        heap = [(0, 0, 0)]
        seen = set()
        result = 0
        
        while heap:
                        
            effort, i, j = heapq.heappop(heap)
            
            result = max(result, effort)
            
            if i == len(heights)-1 and j == len(heights[0])-1:
                return result
            
            seen.add((i, j))
            
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not (x >= 0 <= y) or x >= len(heights) or y >= len(heights[0]):
                    continue
                if (x, y) in seen:
                    continue
                    
                next_effort = abs(heights[i][j] - heights[x][y])                
                heapq.heappush(heap, (next_effort, x, y))
                    
        return 0
    
    