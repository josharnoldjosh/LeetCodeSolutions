class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        M = arr[-1]
        arr = set(arr)
        count = 0
        
        for i in range(1, M+1):            
            if i in arr: continue            
            count += 1
            if count == k:
                return i
            
        return M + k - count
        
    
    
    """
    - m = max(arr) O(n)
    - turn arr to set?
    
    loop over range, count missing numbers...
    if missing count == k: return
    
    else, if we exit range, return max + (k-count)
    
    """