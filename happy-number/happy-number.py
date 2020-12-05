class Solution:
    def isHappy(self, n: int) -> bool:
        
        def cycle(n):
            return sum([int(c) ** 2 for c in str(n)])
        
        count = 0
        
        while(n != 1):          
            n = cycle(n)
            count += 1
            if count > 100:
                return False
                    
        return True
