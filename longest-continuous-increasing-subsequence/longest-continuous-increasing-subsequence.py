class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        best = 0
        replay = [float('inf')]
        for i in nums:
            if replay[-1] >= i:
                replay = [i]
            else:
                replay.append(i)
            best = max(best, len(replay))
        return best