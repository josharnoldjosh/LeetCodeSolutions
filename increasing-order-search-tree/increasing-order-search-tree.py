class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:           
        
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
                
        ans = cur = TreeNode(None)
        
        for i in inorder(root):
            cur.right = TreeNode(i)
            cur = cur.right
            
        return ans.right
                
        
        
    
    
"""
1.
left
current
right

2. 
    2
1       3
"""
        
            