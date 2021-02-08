# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        def recurse(a, b):
            
            if a and b:
                result = TreeNode(a.val+b.val)
            elif a:
                result = TreeNode(a.val)
            elif b:
                result = TreeNode(b.val)
            else:
                return None
            
            result.left = recurse(a.left if a else None, b.left if b else None)
            result.right = recurse(a.right if a else None, b.right if b else None)            
            
            return result
                            
        result = recurse(root1, root2)
        
        return result