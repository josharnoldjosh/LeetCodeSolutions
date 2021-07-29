class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            result += [nums[i]]
        return result