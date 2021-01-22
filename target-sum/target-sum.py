class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        count = collections.Counter({0: 1})
        
        for i in nums:
            step = collections.Counter()
            for j in count:
                step[j+i] += count[j]
                step[j-i] += count[j]
            count = step
            
        return count[S]
        
        
        
"""
    def findTargetSumWays(self, A, S):
        count = collections.Counter({0: 1})
        for x in A:
            step = collections.Counter()
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[S]
"""
