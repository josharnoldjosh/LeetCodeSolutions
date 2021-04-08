class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        durations = list(collections.Counter(tasks).values())
        m = max(durations)
        return max(
            (m-1)*(n+1) + durations.count(m), 
            len(tasks)
        )