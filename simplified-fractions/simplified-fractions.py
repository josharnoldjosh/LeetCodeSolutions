class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
                
        result = []
        
        seen = set()
        
        for num in range(1, n+1):
            for denom in range(num+1, n+1):                
                if (num/denom) not in seen:
                    seen.add(num/denom)
                    result += [f"{num}/{denom}"]
                    
        return result