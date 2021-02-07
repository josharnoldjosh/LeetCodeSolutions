class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def find_target():
            lo, hi = 0, len(nums)
            
            while lo < hi:
                
                mid = (lo + hi) // 2
                
                if nums[mid] == target:
                    return mid
                
                if nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid
                
            return -1
        
        def expand_from_idx(idx):
            i, j = idx, idx
            while i >= 0 and nums[i] == target:
                i -= 1
            while j < len(nums) and nums[j] == target:
                j += 1
            return [i+1, j-1]
        
        idx = find_target()
                
        if idx == -1:
            return [-1, -1]
        
        return expand_from_idx(idx)
    
"""
000001111111100000000
"""