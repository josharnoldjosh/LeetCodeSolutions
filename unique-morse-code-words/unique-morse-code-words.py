class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        graph = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len(set("".join([graph[ord(c) - ord('a')] for c in i]) for i in words))