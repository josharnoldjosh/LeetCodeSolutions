class Solution:
​
    def __init__(self, nums: List[int]):
        self.nums = nums
        
​
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        
​
    def shuffle(self) -> List[int]:        
        shuffled = self.nums[:]
        for i in range(len(shuffled)):
            j = random.randint(0, len(shuffled)-1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
        
​
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
