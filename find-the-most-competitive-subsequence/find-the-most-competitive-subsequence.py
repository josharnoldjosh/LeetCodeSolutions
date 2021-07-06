class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for idx, i in enumerate(nums):                        
            while stack and stack[-1] > i and len(stack) - 1 + len(nums) - idx >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(i)
        return stack