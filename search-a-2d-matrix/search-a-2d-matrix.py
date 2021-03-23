class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(row):
            lo, hi = 0, len(matrix[row])-1
            
            while lo < hi:
                mid = (lo + hi) // 2
                if matrix[row][mid] < target:
                    lo = mid+1
                elif matrix[row][mid] > target:
                    hi = mid
                else:
                    lo = mid
                    break
            
            return lo
        
        
        for row in range(len(matrix)):
            col = search(row)            
            if matrix[row][col] == target:
                return True
            
        return False