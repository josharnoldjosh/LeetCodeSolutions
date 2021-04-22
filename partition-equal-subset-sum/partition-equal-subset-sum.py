class Solution:
    def canPartition(self, nums: List[int]) -> bool:        
        return 0 in functools.reduce(lambda dp, num: {num - i for i in dp} | {num + i for i in dp}, nums, {0})
        
#         dp = {0}
#         for num in nums:
#             dp = {num - i for i in dp} | {num + i for i in dp}        
#         return 0 in dp
    
    
"""
        dp = {0}
        for num in nums:
            dp = {num - i for i in dp} | {num + i for i in dp}        
        return 0 in dp
"""