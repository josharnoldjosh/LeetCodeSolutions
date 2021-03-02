class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:  
        
        queue = collections.deque([i for row in nums for i in row])
        result = []
        
        for _ in range(r):
            row = []
            for _ in range(c):
                try:
                    row += [queue.popleft()]
                except:
                    return nums
            result.append(row)                
        
        return result
    
    
"""
[[1]], 1,1

[[1, 2]]
1, 2
2, 1 (transpose)

[[1, 2, 3]] -> [[1], [2], [3]]

[[1, 2, 3, 4]] 1 row
[[1, 2], [3, 4]] 2 rows
[[1], [2], [3], [4]] 4 rows

- we flatten and read in data...
we just loop over number of rows & consume?

"""