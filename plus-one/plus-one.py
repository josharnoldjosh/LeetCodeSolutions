class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:     
        
        if digits[-1] != 9: return digits[:-1] + [digits[-1]+1]                    
        
        pointer = len(digits)-1
        carry = False
        
        while pointer >= 0:
            
            if digits[pointer] == 9:
                digits[pointer] = 0
                carry = True
            else:
                digits[pointer] += 1
                carry = False
                break
                
            pointer -= 1
            
        if carry:
            return [1] + digits
            
        return digits
