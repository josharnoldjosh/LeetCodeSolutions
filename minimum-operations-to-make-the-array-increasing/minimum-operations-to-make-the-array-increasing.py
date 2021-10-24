class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        score = 0
        i = 0
        while i < len(nums)-1:
            if nums[i] >= nums[i+1]:
                temp = (nums[i] - nums[i+1] + 1)
                nums[i+1] += temp
                score += temp
            else:
                i += 1
                
        return score