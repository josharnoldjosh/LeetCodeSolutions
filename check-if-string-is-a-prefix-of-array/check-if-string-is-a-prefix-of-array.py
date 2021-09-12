class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        for i in range(len(words)+1):
            if s == "".join(words[:i]):
                return True
            
        return False