from collections import (
    deque,
    Counter
)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        result, queue, counts = 0, deque(), Counter()
        
        for i in fruits+[float('inf')]:
            while len(counts.keys()) > 2:
                prev = queue.popleft()
                counts[prev] -= 1
                if counts[prev] == 0:
                    del counts[prev]
            result = max(result, len(queue))
            queue.append(i)
            counts[i] += 1
        
        return result