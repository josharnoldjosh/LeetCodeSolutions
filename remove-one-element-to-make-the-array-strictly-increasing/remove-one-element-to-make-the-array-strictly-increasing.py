class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        
        def skip(nums):            
            for i in range(len(nums)-1):
                if nums[i] >= nums[i+1]:
                    return False            
            return True
        
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return any([
                    skip(nums[i-1:i] + nums[i+1:]),
                    skip(nums[i:i+1] + nums[i+2:]),                    
                ])
            
        return True
                