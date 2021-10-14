from heapq import (
    heappop,
    heapify
)


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        N = len(nums) // 2
        max_heap, min_heap = [-i for i in nums], nums
        heapify(min_heap)
        heapify(max_heap)
        results = []
        for i in range(N):
            results.append(
                -heappop(max_heap) + heappop(min_heap)
            )
        return max(results)
            
        