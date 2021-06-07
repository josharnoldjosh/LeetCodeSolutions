class Solution:
    def convertToTitle(self, num: int) -> str:
        
        graph = {i : chr(i + 65) for i in range(27)}
        
        res = ""
        
        while num > 0:            
            res += graph[(num-1) % 26]
            num = (num-1) // 26
        
                                
        return res[::-1]