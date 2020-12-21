class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result, curr = -float('inf'), 0
        
        for i in nums:
            curr += i
            result = max(result, curr)
            curr = max(0, curr)
            
        return result
            
