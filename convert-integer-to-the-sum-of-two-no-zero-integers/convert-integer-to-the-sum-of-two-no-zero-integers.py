class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
                
        lo = 1
        hi = n-1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if '0' in str(n-mid) + str(mid):
                hi = mid + 1
            else:                
                return [mid, n-mid]
                
        return [lo, n-lo]