# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root: return True
                        
        def in_order(node, depth):
            if not node: return []
            return in_order(node.left, depth+1) + [str(node.val)+str(depth)] + in_order(node.right, depth+1)
        
        return in_order(root.left, 1) == in_order(root.right, 1)[::-1]
