class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        queue = collections.deque([(root, 1)])                
        
        tree = collections.defaultdict(list)
        
        while queue:
            node, depth = queue.popleft()            
            tree[depth] += [node.val if node else None]
            if not node: continue            
            queue.extend([(node.left, depth+1), (node.right, depth+1)])            
                        
        keys = list(sorted(tree.keys()))
        
        a, b = all([all(tree[i]) for i in keys[:-2]]), True
        if len(keys) >= 2:
            x = tree[keys[-2]]            
            found = False
            for i in x:
                if not i:                    
                    found = True
                elif found:
                        return False
                    
        return a and b
    
    
"""
BFS
check if None in level before adding
    if so, return False
"""
        