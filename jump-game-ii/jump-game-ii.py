class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @functools.lru_cache(None)
        def recurse(i, v):            
            if i >= len(nums)-1: return v
            if nums[i] == 0: return float('inf')
            return min([recurse(i+j+1, v+1) for j in range(nums[i])])
        
        return recurse(0, 0)
                
                