class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        
        if b == 0:
            return a if a <= MAX else ~(a ^ mask)
        
        return self.getSum(
            (a ^ b) & mask,
            ((a & b) << 1) & mask
        )
