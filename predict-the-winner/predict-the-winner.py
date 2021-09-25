class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @functools.lru_cache(maxsize=None)
        def recurse(i, j):
            if i > j: return 0
            return max(
                nums[i] - recurse(i+1, j),
                nums[j] - recurse(i, j-1)
            )
        
        return recurse(0, len(nums)-1) >= 0
        