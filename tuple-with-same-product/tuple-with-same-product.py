class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        result, count = 0, collections.Counter()
        
        for i in range(len(nums)):
            for j in range(i):
                key = nums[i]*nums[j]
                result += count[key]
                count[key] += 1
      
        return result*8
