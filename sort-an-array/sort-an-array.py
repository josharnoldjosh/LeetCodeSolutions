class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        pivot = random.choice(nums)
        lt = [i for i in nums if i < pivot]
        eq = [i for i in nums if i == pivot]
        gt = [i for i in nums if i > pivot]
        return self.sortArray(lt) + eq + self.sortArray(gt)