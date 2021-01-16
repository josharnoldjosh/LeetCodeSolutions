class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        
        for i, idx in zip(nums, index):
            result.insert(idx, i)
        
        return result
