class Solution:
    def climbStairs(self, n: int) -> int:
        
        @functools.lru_cache(None)
        def recurse(steps_left):
            if steps_left < 0: return 0
            if steps_left == 0: return 1
            a = recurse(steps_left-1)
            b = recurse(steps_left-2)
            return a+b
        
        return recurse(n)
            