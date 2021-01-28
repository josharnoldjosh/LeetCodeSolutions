class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        
        # Step 1. Build our dp table!
        
        n, m = len(word1)+1, len(word2)+1
        
        dp = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0: dp[i][j] = j
                elif j == 0: dp[i][j] = i        
        
        
        # Step 2. Let's fill this bad boy
        
        for i in range(1, n):
            for j in range(1, m):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) 
               
            
        # Step 3. Return final result
        
        return dp[-1][-1]