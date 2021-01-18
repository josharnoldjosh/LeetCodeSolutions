class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
​
        result = 0
        product = 1
        lagging = 0
​
        for leading in range(len(nums)):
            product *= nums[leading]
            
            while product >= k and lagging <= leading:
                product /= nums[lagging]
                lagging += 1
                
            sub_arr_len = leading - lagging + 1
            result += sub_arr_len
​
        return result
    
​
​
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
​
        prefix, result = [1] + list(itertools.accumulate(nums, operator.mul)), 0
​
        for i in range(1, len(prefix)):                        
            for j in range(0, i):
                if prefix[i] // prefix[j] < k:
                    result += (i-j)
                    break
​
        return result
"""
