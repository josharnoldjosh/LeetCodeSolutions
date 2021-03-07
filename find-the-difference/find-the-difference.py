class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sorted(list(s))
        b = sorted(list(t))
        for i in range(len(s)):
            if a[i] != b[i]:
                return b[i]
        return b[-1]