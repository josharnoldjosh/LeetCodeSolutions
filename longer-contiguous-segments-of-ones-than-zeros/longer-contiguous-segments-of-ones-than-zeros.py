class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        return len(max(s.split("0"), key = len)) > len(max(s.split("1"), key = len))