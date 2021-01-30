class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0: return 0
        
        dp = [1 if i in coins else float('inf') for i in range(amount+1)]
        
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(dp[i], dp[i-c]+1)

        return dp[-1] if dp[-1] < float('inf') else -1
        
            
            
    
    
"""

[1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
[            3, ]

dp[i] = min(
     dp[j] + dp[i-j]
     for j in range(1, i)
        
)

"""