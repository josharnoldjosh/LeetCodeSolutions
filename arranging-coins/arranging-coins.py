class Solution:
    def arrangeCoins(self, n: int) -> int:
        result = 0
        i = 1
        while n >= 0:
            n -= i
            i += 1
            result += int(n >= 0)
        return result