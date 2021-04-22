class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {0}
        for num in nums:
            dp = {num - i for i in dp} | {num + i for i in dp}        
        return 0 in dp
    
    
"""
- We have an array
- Elements have "value"
- Given a function, in this case, sum(x), we want to minimize the absolute difference between two subsets
"""
