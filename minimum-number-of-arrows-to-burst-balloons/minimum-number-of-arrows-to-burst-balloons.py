class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        A = collections.deque([range(i, j+1) for i, j in sorted(points)])
        f = lambda x, y: range(max(x[0], y[0]), min(x[-1], y[-1])+1)
        result = 1
        
        while A:
            i = A.popleft()
            
            while A and i:     
                i = f(i, A[0])
                if not i: result += 1
                else: A.popleft()
                    
        return result
        