class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if nums == []: return 0
        
        idx, count = 0, 0
        
        while True:            
            if idx == len(nums)-1: break
            if nums[idx] == nums[idx+1]:                
                nums[idx], nums[count] = nums[count], nums[idx]
                count += 1
            idx += 1            
                
        nums[:] = sorted(nums[count:])
        return len(nums)
                
