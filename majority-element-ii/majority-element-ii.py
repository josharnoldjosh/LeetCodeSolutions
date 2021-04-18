class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [key for key, val in collections.Counter(nums).items() if val > len(nums) / 3]