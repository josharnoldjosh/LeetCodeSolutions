class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        N = len(candyType) // 2
        return min(len(set(candyType)), N)
        
        