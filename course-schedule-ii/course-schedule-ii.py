class Solution:
    
    def build_graph(self, prerequisites):↔​
            
    def dfs(self, i):
        # Base case
        if self.visited[i] == -1: return False        
        if self.visited[i] == 1: return True
        
        self.visited[i] = -1 # start our search here ------
        
        for x in self.graph[i]:
            if not self.dfs(x):
                return False
            
        self.visited[i] = 1 # end our search here ------
        self.result.append(i)
        return True
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        self.build_graph(prerequisites)        
        self.visited = [0 for i in range(numCourses)]
        self.result = []
        
        for i in range(numCourses):
            if not self.dfs(i):
                return []
            
        return self.result
        
        
            
        
            
​
        
                
    
        
