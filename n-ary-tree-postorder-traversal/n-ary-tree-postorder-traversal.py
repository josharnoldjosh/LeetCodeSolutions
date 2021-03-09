"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        global result
        result = []
        
        def recurse(node):
            if not node: return
            for i in node.children:
                recurse(i)
            result.append(node.val)
            
        recurse(root)        
        return result