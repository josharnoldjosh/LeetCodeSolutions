class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:                
        
        i = 0
        prev = float('inf')
        count = 1
        
        while True:
            
            try: nums[i]
            except: break
                                        
            if prev != nums[i]:
                prev = nums[i]
                count = 1
            else:                
                count += 1
                
            if count >= 3:
                del nums[i-1]
            else:
                i += 1
                
