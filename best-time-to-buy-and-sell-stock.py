class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        result, prev = 0, float('inf')
        for i in prices:
            if i < prev: prev = i
            result = max(result, i - prev)            
        return result                    
