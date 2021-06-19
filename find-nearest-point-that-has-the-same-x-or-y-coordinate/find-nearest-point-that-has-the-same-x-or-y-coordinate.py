class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        return min([
            (abs(x-i) + abs(y - j), idx)
            for idx, (i, j) in enumerate(points)
            if x == i or j == y
        ] + [(float('inf'), -1)])[1]