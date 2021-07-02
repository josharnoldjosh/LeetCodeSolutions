class Solution:
            
    def validPalindrome(self, s: str) -> bool:        
        
        def greedy(a, b):            
            idx, jdx, error, e = 0, 0, 0, ''
            while idx < len(a):                
                if a[idx] == b[jdx]:                    
                    idx += 1
                    jdx += 1                    
                elif not error:
                    e = a[idx]
                    idx += 1
                    error = 1                    
                else:                    
                    if error == 1 and e == b[jdx]:                        
                        error += 1
                        jdx += 1                 
                        continue
                    else:
                        return False                  
            return True
                
                
        return greedy(s, s[::-1]) or greedy(s[::-1], s)
                
        
"""
e = b
error = 2

a
ba

"""