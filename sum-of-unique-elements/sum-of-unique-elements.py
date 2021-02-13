class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:        
        return sum([x[0] for x in collections.Counter(nums).items() if x[1] == 1]+[0])