class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:        
        intervals.sort()
        return all(
            i[1] <= j[0]
            for i, j in zip(intervals[:-1], intervals[1:])
        )