import math
​
​
class Solution:
    def trailingZeroes(self, n: int) -> int:        
        ans = 0        
        for i in str(math.factorial(n))[::-1]:
            if i == "0": ans += 1
            else: break        
        return ans                
