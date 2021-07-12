"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        children = set()
        
        @functools.lru_cache(None)
        def dfs(node):
            if not node: return
            for i in node.children:
                children.add(i)
                dfs(i)
                
        for i in tree:
            dfs(i)
                                       
        return list((set(tree) - children))[0]