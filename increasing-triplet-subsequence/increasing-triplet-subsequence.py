class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        i = j = float('inf')
        
        for n in nums:
            if n <= i:
                i = n
            elif n <= j:
                j = n
            else:
                return True
            
        return False
    
"""
just take permutation of size 3 from indices and check if valid subsequence.
"""

"""
Brute Force

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i, j, k in itertools.permutations(list(range(len(nums))), 3):
            if i < j < k and nums[i] < nums[j] < nums[k]:
                return True
        return False
        
        
  
10, 11, 1, 2, 3
i   j   i  j. k

10, 11, 1, 2, 12



def increasingTriplet(nums):
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False
"""