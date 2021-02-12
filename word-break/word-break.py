class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        global result
        result = False
        
        
        # Build a graph of "sorts"
        graph = collections.defaultdict(set)
        for word in wordDict:
            graph[word[0]].add(word)
            
        
        @functools.lru_cache(maxsize=None)
        def recurse(s):
            global result
            
            # Termination condition 1)
            if result == True:
                return
            
            # Termination condition 2)
            c = s[0:1]
            if c == "":
                result = True
                return
            
            # Termination condition 3)
            if len(graph[c]) == 0:
                return
            
            # See which words are in here
            for word in graph[c]:
                if s[0:len(word)] == word:
                    recurse(s[len(word):])
                
                
        recurse(s)
                
        return result
        
    
"""

- start at character
- recursively read possibilities from a trie?

- needs to be recursive
- mark global variable as success
- return global variable


helloworld
[hello, helloworld]
"""