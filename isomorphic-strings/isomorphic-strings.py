class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def build_sequence(s):
            graph = {}
            stack = [i for i in range(len(set(s)))]
            result = []
            for c in s:
                if c not in graph:
                    graph[c] = stack.pop()
                result.append(graph[c])
            return result
        
        return build_sequence(s) == build_sequence(t)