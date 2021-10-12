class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return list(heapq.nlargest(k, nums, key = lambda x: int(x)))[-1]