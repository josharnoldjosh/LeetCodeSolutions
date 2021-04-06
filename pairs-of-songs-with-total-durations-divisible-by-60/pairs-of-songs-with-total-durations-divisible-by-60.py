class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:        
        seen, result = [0] * 60, 0  
        for i in time:
            result += seen[-i % 60]
            seen[i % 60] += 1
        return result