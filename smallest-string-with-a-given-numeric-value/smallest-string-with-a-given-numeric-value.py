class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        k -= n
        
        if k == 0:
            return "a"*n
    
        mapping = {i+1 : c for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        
        result = ["a"]*n
        idx = -1
    
        while k != 0:
            k += 1
            key = min(k, 26)
            letter = mapping[key]
            result[idx] = letter
            idx -= 1
            k -= key
            
        return "".join(result)