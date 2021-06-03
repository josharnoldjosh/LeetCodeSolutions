class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        result = collections.defaultdict(int)
        for i in arr:
            result[i] = result[i - difference] + 1
        return max(result.values())
        
        
    
"""
Return an int

- either pick an element or skip an element
"""