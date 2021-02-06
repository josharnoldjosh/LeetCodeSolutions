class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        lo, hi = 0, len(arr)
        
        while lo < hi:
            
            m = (lo+hi) // 2
            
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            
            if arr[m-1] < arr[m]:
                lo = m
            else:
                hi = m+1
                
        return -1