class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        i, white, blue = 0, 0, 0
        
        while i < len(nums):
            
            if nums[i] == 1:
                del nums[i]
                white += 1            
            elif nums[i] == 2:
                del nums[i]
                blue += 1
            else:
                i += 1
                
        nums += [1]*white + [2]*blue
    
