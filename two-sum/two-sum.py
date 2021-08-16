class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        dp = {}
        for idx, i in enumerate(nums):
            if target-i in dp:
                return [dp[target-i], idx]
            dp[i] = idx
        raise Exception("Invalid testcase")
                