class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        mapping = {}
        
        if len(s.split()) != len(pattern):
            return False
        
        for idx, word in enumerate(s.split()):
            c = pattern[idx]
            
            if word in mapping and mapping[word] != c:
                return False
            
            if word in mapping and mapping[word] == c:
                continue
            
            if word not in mapping and c not in mapping.values():
                mapping[word] = c
            else:
                return False
            
        
        return True