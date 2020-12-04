class Trie:
​
    def __init__(self):
        self.all_items = set()
        self.prefix = set()        
​
    def insert(self, word: str) -> None:
        self.all_items.add(word)
        for i in range(1, len(word)+1):
            self.prefix.add(word[:i])        
​
    def search(self, word: str) -> bool:
        return word in self.all_items
        
    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix
        
​
​
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
