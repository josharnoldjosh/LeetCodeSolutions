class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s).values()
        return sum([i if i % 2 == 0 else i-1 for i in counts]) + (len([i for i in counts if i%2 != 0]) != 0) 