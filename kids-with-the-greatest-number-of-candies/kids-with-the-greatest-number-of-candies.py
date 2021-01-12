class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        if not candies: return []
        
        best = max(candies)
        
        ans = [False]*len(candies)
        
        for idx, i in enumerate(candies):
            if i+extraCandies >= best:
                ans[idx] = True
                
        return ans
