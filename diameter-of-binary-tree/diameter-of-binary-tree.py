class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def recurse(node):
            if not node: return 0
            left, right = recurse(node.left), recurse(node.right)
            self.result = max(self.result, left+right)
            return 1 + max(left, right)
    
        self.result = 0
        recurse(root)
        return self.result
    
    
"""
on the result level, we sum the left and right values...
on the return level, we go as far left and as far right as possible...?
"""
