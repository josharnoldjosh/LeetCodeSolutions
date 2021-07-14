class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0, 0)}
        x, y = 0, 0
        graph = {"N": 1, "S": -1, "W": -1, "E": 1}
        for c in path:            
            x += graph[c] if c in "WE" else 0
            y += graph[c] if c in "NS" else 0
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False
            
        