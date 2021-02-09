# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def recurse(node, min, max):
            if not node: return True
            if not (min < node.val < max): return False
            return recurse(node.left, min, node.val) and recurse(node.right, node.val, max)
        
        return recurse(root, -float('inf'), float('inf'))