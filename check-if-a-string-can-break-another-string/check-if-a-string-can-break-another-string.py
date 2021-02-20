class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        a = [ord(i) for i in s1]
        b = [ord(j) for j in s2]
        
        a.sort()
        b.sort()
        
        a_breaks_b = True
        b_breaks_a = True
        
        for i in range(len(min(a, b))):
            if a[i] < b[i]:
                a_breaks_b = False                
            if a[i] > b[i]:
                b_breaks_a = False
                
        return a_breaks_b or b_breaks_a
            
    
        
"""
covert to array of ord, then sort?
"""