class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        dp = {}        
        for idx, i in enumerate(nums):
            if target-i in dp and dp[target-i] != idx:
                return [idx, dp[target-i]]
            dp[i] = idx
        return -1
            
        
                