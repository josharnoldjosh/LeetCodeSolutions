class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()
        
        @functools.lru_cache(maxsize=None)
        def longest_chain(idx):
            if idx == len(pairs)-1:
                return 1
            results = [float('-inf')]
            for jdx in range(idx+1, len(pairs)):
                if pairs[idx][1] < pairs[jdx][0]:
                    results += [longest_chain(jdx) + 1]
            return max(results)
                    
        return max(        
            longest_chain(idx)
            for idx in range(len(pairs))
        )
        
"""
sort by start?
"""