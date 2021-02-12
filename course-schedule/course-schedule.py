class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                
        
        def dfs(course):  
            if seen[course] == 1: return True
            if seen[course] == -1: return False
            seen[course] = -1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            seen[course] = 1
            return True
        
                                        
        # Create graph
        graph = collections.defaultdict(list)        
        for b, a in prerequisites: graph[a] += [b]
            
        # Seen
        seen = collections.defaultdict(int)
                        
        # Dfs on each course        
        return all([dfs(course) for course in range(numCourses)])