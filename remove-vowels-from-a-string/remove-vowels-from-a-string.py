class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {c for c in "aeiou"}        
        return ''.join([c for c in s if c not in vowels])