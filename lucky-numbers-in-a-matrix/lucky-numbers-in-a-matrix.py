class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:        
        rows = [min(r) for r in matrix]
        cols = [max(c) for c in zip(*matrix)]        
        return set(rows) & set(cols)
        