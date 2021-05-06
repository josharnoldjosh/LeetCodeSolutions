class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:      
        graph = {c : i for i, c in enumerate(order)}
        return words == sorted(words, key = lambda word: [graph[c] for c in word])        
    
        