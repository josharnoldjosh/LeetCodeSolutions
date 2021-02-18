class Solution:
    
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
                
        s = 0
        g = lambda i, j: mat[i][j] if i >= 0 <= j else 0
                
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] += g(i-1, j) + g(i, j-1) - g(i-1, j-1)         
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):                
                if i >= s <= j:
                    if g(i, j) - g(i-s-1, j) - g(i, j-s-1) + g(i-s-1, j-s-1) <= threshold:
                        s += 1
                                        
        return s
        
        