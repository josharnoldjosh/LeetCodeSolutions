class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
                    
        def recurse(node):            
            if not node: return None            
            if node.val == p.val or node.val == q.val: return node            
            l, r = recurse(node.left), recurse(node.right)
            if l and r: return node
            if l: return l
            if r: return r
                                    
        return recurse(root)
        
                
            
    
    
"""
Cases:
​
A
​
   B
   
   
   B
​
A
​
​
    X
    
A
​
        B
​
"""
