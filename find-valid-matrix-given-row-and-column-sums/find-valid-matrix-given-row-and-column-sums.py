class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        M, N = len(rowSum), len(colSum)
        
        result = [[0 for _ in range(N)] for _ in range(M)]                
                
        for i in range(M):
            for j in range(N):
                val = min(rowSum[i], colSum[j])
                rowSum[i] -= val
                colSum[j] -= val                
                result[i][j] = val    
        
        return result    