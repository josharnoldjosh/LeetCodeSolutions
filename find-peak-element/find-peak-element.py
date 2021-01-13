class Solution:
    def findPeakElement(self, nums: List[int]) -> int:        
        best = max(nums)
        idx = nums.index(best)
        return idx
                
            
