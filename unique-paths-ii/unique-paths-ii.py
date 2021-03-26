class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        
        # Init dp grid full of zeros
        dp = [[0]*N for _ in range(M)]
        
        # Set first value of dp
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        # DP Equation
        for i in range(M):
            for j in range(N):                                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] += (dp[i-1][j] if i-1 >= 0 else 0)
                dp[i][j] += (dp[i][j-1] if j-1 >= 0 else 0)
                                    
        return dp[-1][-1]