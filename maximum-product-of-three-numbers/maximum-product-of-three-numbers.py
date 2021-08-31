from functools import reduce
from operator import mul

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        return max(
            reduce(mul, nums[-3:]),
            reduce(mul, nums[:2] + [nums[-1]])
        )