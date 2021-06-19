class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1        
        result = []
        for pivot in range(1, len(arr)):                        
            l = arr[:pivot]
            r = arr[pivot:]
            if sorted(l) + sorted(r) == sorted(arr):
                result += [self.maxChunksToSorted(l) + self.maxChunksToSorted(r)]
        return max(result) if result else 1
    
"""
if len(nums) <= 1: return nums
pivot = random.choice(nums)
lt = [i for i in nums if i < pivot]
eq = [i for i in nums if i == pivot]
gt = [i for i in nums if i > pivot]
return self.sortArray(lt) + eq + self.sortArray(gt)
"""