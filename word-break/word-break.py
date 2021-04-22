class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @functools.lru_cache(None)
        def recurse(s):
            if s in wordDict: return True
            return any([
                recurse(s[:idx]) and recurse(s[idx:]) 
                for idx in range(len(s))
            ])
                
        return recurse(s)
            
        
"""
Really, its about choose a place to break the word...

say you have ["leet", "code", "leetcode"]
"""