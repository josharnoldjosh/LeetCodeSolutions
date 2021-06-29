class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:              
        
        result = square = no_square = 0
        
        for i in nums:
            a = max(no_square+i, i)
            b = max(no_square + i**2, i**2, square + i)
            result = max(result, b)
            no_square, square = a, b        
        
        return result


"""
Brute force:

```python
def score(idx):            
    a = itertools.accumulate([0] + nums[:idx][::-1])
    b = itertools.accumulate([0] + nums[idx+1:])
    return max(a) + (nums[idx] ** 2) + max(b)

return max([
    score(idx)
    for idx in range(len(nums))            
])
```
"""