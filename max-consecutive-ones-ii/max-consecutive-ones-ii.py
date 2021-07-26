class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return 1
        
        sums = [0]
        
        for i in nums:
            if i == 0:
                sums += [0]
            else:
                sums[-1] += i
                
        return max(
            sum(sums[i:i+2]) + (len(sums[i:i+2]) == 2)
            for i in range(len(sums))
        )
        
        
        
"""

xxxxxx 0 xxxxxxx 0

2 3 1 4

"""