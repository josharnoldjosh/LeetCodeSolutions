class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        M, N = len(mat), len(mat[0])
        
        result = 0
        
        mat_t = list(zip(*mat))
        
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 1 and \
                sum(mat[i]) == 1 and \
                sum(mat_t[j]) == 1:
                    result += 1
                    
                
        return result
                
        
"""
[
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,1,0,0]]
"""