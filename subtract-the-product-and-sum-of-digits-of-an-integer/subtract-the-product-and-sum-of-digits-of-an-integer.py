import functools

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        p = functools.reduce(lambda x, y: x*y, digits)
        s = sum(digits)
        return p - s
        