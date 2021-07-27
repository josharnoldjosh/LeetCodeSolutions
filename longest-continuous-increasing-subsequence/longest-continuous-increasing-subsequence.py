class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        best = 0
        replay = float('inf')
        score = 0
        for i in nums:
            if replay >= i:
                score = 0
            replay = i            
            score += 1
            best = max(best, score)
        return best