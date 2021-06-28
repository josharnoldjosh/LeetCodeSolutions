"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
                
        if not root: return []
            
        queue = collections.deque([(root, 0)])        
        d = collections.defaultdict(list)
        
        while queue:
            node, level = queue.popleft()                
            d[level].append(node.val)
            queue.extend([(i, level+1) for i in node.children])
            
        return d.values()
            