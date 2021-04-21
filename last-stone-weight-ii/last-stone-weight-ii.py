from functools import reduce

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        f = lambda dp, y: {y + i for i in dp} | {abs(y-i) for i in dp}
        return min(reduce(f, stones, {0}))
        
        # dp = {0}
        # for stone in stones:
        #     dp = {stone + i for i in dp} | {abs(stone - i) for i in dp}
        # return min(dp)
    
"""
dp = {0}
for a in A:
    dp = {a + x for x in dp} | {abs(a - x) for x in dp}
return min(dp)
"""