class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
                 
        result = 0
        sums = 0
        dp = collections.defaultdict(int, {0 : 1}) 
        
        for i in range(len(nums)):
            sums += nums[i]
            result += dp[sums - k]
            dp[sums] = dp[sums] + 1 
                        
        return result
    
    
    
"""
Brute force!
* I use padding to do extra calculations but to make sure we don't miss any window sizes/alignments
* Sure, padding uses extra computation but its not a big deal
* `if not nums` is used to skip counting any "empty" slices
* We use a set to make sure each window is unique
* TLE's, obviously

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        padding = 10
        result = set()        
        
        for window_size in range(len(nums)+padding):            
            for i in range(len(nums)+padding):
                if not nums[i:i+window_size]: continue
                if sum(nums[i:i+window_size]) == k:
                    result.add((i, min(window_size+i, len(nums))))
                                    
        return len(result)
```

First Improvement: Prefix sum array

* Passes more test cases, but still eventually TLE's

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
                        
        result, prefix = 0, list(itertools.accumulate([0] + nums))
                        
        for window_size in range(1, len(prefix)):
            for pos in range(0, len(prefix)-window_size):                
                if k == prefix[pos+window_size] - prefix[pos]:
                    result += 1
        
        return result
```
"""