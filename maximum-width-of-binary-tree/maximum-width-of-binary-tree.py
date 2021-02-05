class Solution:
    
    def widthOfBinaryTree(self, root: TreeNode) -> int:        
        
        def dfs(node, level, x):
            if node:
                yield level, x
                yield from dfs(node.left, level+1, 2*x)
                yield from dfs(node.right, level+1, (2*x)+1)
                    
        level_min = {}
        level_max = {}
        
        result = 0
        
        for depth, pos in dfs(root, 0, 0):
            level_min[depth] = min(level_min.get(depth, pos), pos)
            level_max[depth] = max(level_max.get(depth, pos), pos)
            result = max(result, 
                         level_max[depth] - level_min[depth] + 1) 
        
        return result
    
    
"""
dfs w/ coordinate
"""