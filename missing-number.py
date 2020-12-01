class Solution:
    
    def missingNumber(self, nums: List[int]) -> int:
        return self.fib(len(nums)) - sum(nums)
    
    def fib(self, n):
        if n == 0: return 0
        return n + self.fib(n-1)
    
    
