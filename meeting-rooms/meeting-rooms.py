class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        result = []
        
        for i in sorted(intervals, key=lambda x: x[0]):
            if not result or result[-1][1] <= i[0]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1])
                
        return len(result) == len(intervals)