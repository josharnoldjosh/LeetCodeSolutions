class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                        
        graph = collections.defaultdict(list)        
        
        for a, b in prerequisites:
            graph[a].append(b)
            
        visited = {i:0 for i in range(0, numCourses)}
        
        def dfs(i):
            if visited[i] == 1: return True
            if visited[i] == -1: return False
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
