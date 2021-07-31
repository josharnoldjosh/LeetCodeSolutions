class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counts = collections.Counter(s)
        heap = [(-v, k) for k, v in counts.items()]
        heapq.heapify(heap)
        
        result = ""
        
        if not heap:
            return ""
        
        count, key = heapq.heappop(heap)
                
        while heap or count:            
            if count < 0:
                result += key
                count += 1                
            if count < 0 and heap:
                (count, key) = heapq.heapreplace(heap, (count, key))
            elif count < 0 and not heap:
                result += "".join([key]*abs(count))
                count = 0                
            elif heap:
                (count, key) = heapq.heappop(heap)                
                     
        for key, group in itertools.groupby(result):
            if len(list(group)) >= 2:
                return ""
            
        return result
        
        
"""

"""