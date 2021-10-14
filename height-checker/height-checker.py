class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum([
            1 
            if heights[i] != expected[i]
            else 0
            for i in range(len(heights))
        ])