class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
                
        """
        Build a graph mapping numerator -> [(denominator, value), ...],
        and vice versa
        """
        global graph
        graph = collections.defaultdict(list)        
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1/v))
            
        
        """
        Hop through the graph!
        """
        def compute_query(a, b):
            global graph
            
            if a not in graph or b not in graph:
                return -1.0

            if a == b:
                return 1.0

            seen = set()

            def dfs(x):
                if x in seen:
                    return -float('inf')
                if x == b:
                    return 1.0
                seen.add(x)
                result = max([v*dfs(y) for y, v in graph[x]])
                seen.remove(x)
                return result

            result = dfs(a)
            
            return result if result != -float('inf') else -1.0
        
                    
        """
        Compute all the queries!
        """
        result = []
        for a, b in queries:
            result += [compute_query(a, b)]
                    
        return result
    
    
    
    
    
    
    
"""
1) generate as many values from start
    - return look up

b/a
a/b
c/b
b/c
-> a/c
-> c/a

Another question: how do we know we CAN'T find a successful result?
1) numerator or denominator not in our list of values?
2) not so obvious...

Graph

a/c

{
    a : [(b, 2.0)],
    b : [(c, 3.0)],
    b : [(a, 1/2.0)],
    c : [(b, 1/3.0)]
}
"""