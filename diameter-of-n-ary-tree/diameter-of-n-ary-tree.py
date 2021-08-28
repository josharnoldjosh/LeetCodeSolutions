"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
                    
        def sink(node):
            if not node: return 0  
            results = [
                1 + sink(i)
                for i in node.children
            ]            
            return max(results+[0])
        
        best = 0
        
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            result = sum(sorted([
                1 + sink(i)
                for i in node.children
            ], reverse=True)[:2])
            
            best = max(best, result)
            
            queue.extend(node.children)
            
        return best
        