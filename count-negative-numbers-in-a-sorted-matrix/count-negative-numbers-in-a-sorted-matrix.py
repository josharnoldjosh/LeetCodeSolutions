class Solution:    
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        def binary_search(row, target, lo, hi):            
            while lo < hi:
                mid = (lo+hi) // 2
                if row[mid] > target:
                    lo = mid+1
                else:
                    hi = mid
            return lo
                
        result = 0
        
        for row in grid:
            result += len(row) - binary_search(row, -1, 0, len(row))
                        
        return result