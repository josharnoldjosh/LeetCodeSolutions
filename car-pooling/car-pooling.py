class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        end_location = max([i[-1] for i in trips]) + 1
        queue = [0] * end_location
        
        for i in trips:
            (count, start, end) = i 
            queue[start] += count
            queue[end] -= count
            
        queue = collections.deque(queue)
        
        current_passengers = 0
        
        while queue:            
            if current_passengers > capacity: return False
            current_passengers += queue.popleft()            
            
        return True
        