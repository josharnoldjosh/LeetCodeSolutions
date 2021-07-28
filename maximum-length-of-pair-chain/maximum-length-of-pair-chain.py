class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()

        @functools.lru_cache(maxsize=None)
        def longest_chain(idx):
            if idx == len(pairs)-1:
                return 1 
            return 1 + max(
                [
                    longest_chain(jdx)
                    if pairs[idx][1] < pairs[jdx][0]
                    else
                    float('-inf')
                    for jdx in range(idx+1, len(pairs))                    
                ]
            )

        return max(
            longest_chain(idx)
            for idx in range(len(pairs))
        )
        
"""
sort by start?
"""