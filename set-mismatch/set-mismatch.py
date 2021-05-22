class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = collections.Counter(nums).most_common(1)[0][0]
        nums = set(nums)
        for i in range(1, max(nums)+2):
            if i not in nums:
                return [dup, i]
        