class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        best = -1
        
        for idx, i in enumerate(nums):
            for jdx, j in enumerate(nums):
                if idx == jdx:
                    continue
                best = max(best, i+j if i+j < k else -1)
                    
        return best
                    
                
            
            
            