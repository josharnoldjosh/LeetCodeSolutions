class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        dp = {0}
        
        for i in nums:
            dp = {i+j for j in dp} | {abs(i-j) for j in dp}
            
        return not min(dp)