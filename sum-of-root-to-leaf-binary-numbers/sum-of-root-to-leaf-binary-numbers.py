class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        result = [0]
        
        def recurse(node, res):            
            if not node: return            
            if node and not node.left and not node.right:                
                result[0] += int(res+str(node.val), 2)
                return            
            recurse(node.left, res+str(node.val))
            recurse(node.right, res+str(node.val))
                        
        recurse(root, "")        
        return result[0]