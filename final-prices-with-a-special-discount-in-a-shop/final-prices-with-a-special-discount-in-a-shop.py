class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:        
            
        def get_j(i):
            for j in range(i+1, len(prices)):
                if j > i and prices[j] <= prices[i]:
                    return prices[i] - prices[j]
            return prices[i]
                
        return [get_j(i) for i in range(len(prices))]
            