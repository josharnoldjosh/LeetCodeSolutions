class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = collections.defaultdict(lambda: 1)
        N = len(A)
        for i in range(N):
            for j in range(i+1, N):
                diff = A[j] - A[i]
                dp[j, diff] = dp[i, diff] + 1
        return max(dp.values())