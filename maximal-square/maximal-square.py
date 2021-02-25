class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
                
        def square_sum(i, j, size):
            result = 0
            for row in range(i, i+size):
                try:
                    result += sum([1 if x == "1" else 0 for x in matrix[row][j:j+size]])                
                except:
                    return 0
            return result
                
        def expand(i, j):
            best = 0
            size = 1
            expected_sum = 1
            while True:
                result = square_sum(i, j, size)
                if result != expected_sum:
                    return best
                best = result
                size += 1
                expected_sum = size ** 2                
                                
        best = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                best = max(best, expand(i, j))
            
        return best
    
        
    
"""
Largest square
- square
    - expanding square from source?
    
How do we expand the square?
We can compare sums?
expected sum == sum(square) ?
One extra row, one extra column
"""