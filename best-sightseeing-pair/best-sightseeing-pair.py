class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:        
        cur = res = 0
        for x in values:
            res = max(res, cur + x)
            cur = max(cur, x) - 1
        return res