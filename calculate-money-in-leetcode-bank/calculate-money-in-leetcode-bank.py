class Solution:
        
    def totalMoney(self, n: int) -> int:        
        result = 0
        for i in range(n//7):
            result += self.accumulate(i+1)
        result += self.accumulate(bias = (n // 7)+1, num_days = n % 7)            
        return result
    
    def accumulate(self, bias=1, num_days=7):
        return sum([bias+i for i in range(num_days)])
                 
        