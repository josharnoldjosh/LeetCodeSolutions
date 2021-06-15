"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        seen = set()
        
        while p:
            seen.add(p)
            p = p.parent

        while q:
            if q in seen:
                return q
            q = q.parent
                        
        return None
            
        
"""
Cases:
- both have equal distance to parent
    - parent, parent, parent, if equal, return...
- p has longer path than q
    - go up p
    - go up q, if q in seen_p, return!
- q has longer path than p

"""        
