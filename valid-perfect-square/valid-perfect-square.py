class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num = str(num ** 0.5)
        trail = num[len(num)-2:]
        return trail == ".0"