# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
                
        lo, hi = 1, n+1
        
        while lo < hi:
            
            mid = (lo + hi) // 2
            
            result = guess(mid)            
            
            if result == 0:
                return mid            
            elif result == 1:
                lo = mid+1                                
            elif result == -1:
                hi = mid                
                
        return 0