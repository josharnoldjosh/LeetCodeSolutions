class Solution:
    def minMoves2(self, nums: List[int]) -> int:        
        median = statistics.median_low(nums)
        return sum([
            abs(i-median)
            for i in nums
        ])
    
        
    
    
"""
Minimum implies
- greedy
- dp
- backtracking

[1,10,2,9]

1,2,9,10

  
  
"""