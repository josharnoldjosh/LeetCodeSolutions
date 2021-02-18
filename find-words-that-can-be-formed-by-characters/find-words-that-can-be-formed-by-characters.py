from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        result = 0
        counts = Counter(chars)
        
        for word in words:
            result += len(word)
            word_counts = Counter(word)
            for char, count in word_counts.items():
                if count > counts[char]:
                    result -= len(word)
                    break
                                
        return result