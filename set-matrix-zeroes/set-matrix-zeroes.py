class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.        
        """
        
        M, N = len(matrix), len(matrix[0])
        
        zeros = []
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        
        def dfs(i, j, di, dj):
            if not (0 <= i < M) or not (0 <= j < N):
                return
            matrix[i][j] = 0
            dfs(i+di, j+dj, di, dj)
        
        while zeros:
            i, j = zeros.pop()
            dfs(i, j, 0, 1)
            dfs(i, j, 0, -1)
            dfs(i, j, 1, 0)
            dfs(i, j, -1, 0)
        
        
        