class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        result = 0
        
        for idx, i in enumerate(nums):
            for jdx, j in enumerate(nums):
                if idx >= jdx: continue
                if i == j: result += 1
                    
        return result
                
