class Wrapper:
    
    def __init__(self, node):
        self.node = node            

    def make_tuple(self):                
        def dfs(i, s):
            if not i: return None
            dfs(i.left, s="left")
            self.result += [(i.val, s) if i else None]
            dfs(i.right, s="right")
        self.result = []
        dfs(self.node, "rot")
        return tuple(self.result)

    def __hash__(self):
        return hash(self.make_tuple())

    def __eq__(self, other):   
        return self.make_tuple() == other.make_tuple()
    
        
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        counts = collections.Counter()
                                    
        def dfs(node):
            if not node: return
            dfs(node.left)            
            counts[Wrapper(node)] += 1 # need a representation
            dfs(node.right)
            
        dfs(root)
                                            
        return [i.node for i, count in counts.items() if count > 1]
            
    
    
"""
- dfs the tree,

add each node to a dict

value -> list[node, node, node]
"""