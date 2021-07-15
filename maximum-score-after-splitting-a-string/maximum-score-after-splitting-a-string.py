from collections import Counter


class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score = max(
                score, 
                Counter(s[:i])["0"] + Counter(s[i:])["1"]
            )
        return score