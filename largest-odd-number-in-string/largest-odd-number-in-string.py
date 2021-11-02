class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        for idx, i in enumerate(num[::-1]):
            if i in "13579":                            
                return num[:len(num)-idx]
            
        return ""
            
        
