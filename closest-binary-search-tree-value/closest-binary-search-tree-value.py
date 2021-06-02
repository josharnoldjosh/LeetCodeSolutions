# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        global data
        data = [float('inf'), -1]
        
        def recurse(node):
            global data
            if not node: return
            recurse(node.left)
            key = abs(node.val - target)
            if key < data[0]: data = [key, node.val]            
            recurse(node.right)
            
        recurse(root)
        
        return data[-1]
        