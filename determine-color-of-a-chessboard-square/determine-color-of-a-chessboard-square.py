class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
                                                                                        
        (char, num) = coordinates
        
        offset = ord(char) % 2 == 0
        
        return int(num) % 2 == offset