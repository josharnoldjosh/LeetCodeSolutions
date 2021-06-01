class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        diff = int((arr[-1] - arr[0]) / len(arr))
                        
        for idx in range(1, len(arr)):
            if arr[idx] - arr[idx-1] != diff:
                return arr[idx-1] + diff        
        
        return arr[-1]