class Solution:
    def minOperations(self, n: int) -> int:
        
        result = []
        count = 0        
        for i in range(n):
            result.append((2*i)+1)
            
            
        val = result[len(result)//2]
            
        if len(result) % 2 == 0:
            idx = len(result)//2
            val = (result[idx] + result[idx-1]) // 2
                                                
        for i in range(len(result)//2):
            count += val-result[i]
            
        return count
    