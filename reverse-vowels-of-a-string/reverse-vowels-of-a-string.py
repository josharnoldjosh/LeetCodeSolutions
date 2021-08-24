class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set([c for c in "aeiouAEIOU"])
        
        stack = []
        
        for c in s:
            if c in vowels:
                stack.append(c)
                
        result = ""
        
        for c in s:
            if c in vowels:
                result += stack.pop()
            else:
                result += c
        
        return result