class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dp = {}
        for idx, i in enumerate(nums):
            dp[i] = idx
            
        for idx, i in enumerate(nums):
            key = target-i
            if key in dp and dp[key] != idx:
                return [idx, dp[key]]
                        
        return []
