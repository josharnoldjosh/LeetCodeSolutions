class Solution:
    def canPartitionKSubsets(self, nums, k):
        target, m = divmod(sum(nums), k)
        if m: return False

        dp, N = [0] * k, len(nums)
        
        nums.sort(reverse=True)
        
        
        def dfs(i):            
            # All buckets have same sum
            if i == N: return len(set(dp)) == 1
            
            # For each bucket
            for j in range(k):
                dp[j] += nums[i]
                if dp[j] <= target and dfs(i+1):
                    return True
                dp[j] -= nums[i]
                
                if not dp[j]: break # not sure about this line
            return False
        
        return nums[0] <= target and dfs(0)