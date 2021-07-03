class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        result = []
        counts = collections.Counter(barcodes)
        heap = [[-v, k] for k, v in counts.items()]
        heapq.heapify(heap)
                   
        item = heapq.heappop(heap)
            
        while heap:
            result += [item[1]]
            item[0] += 1
            item = heapq.heapreplace(heap, [item[0], item[-1]]) if item[0] < 0 else heapq.heappop(heap)
            
        result += [item[1]]
                        
        return result