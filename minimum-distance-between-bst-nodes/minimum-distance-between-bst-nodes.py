# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        values = []
        
        def dfs(node):
            if not node: return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        values.sort()
        
        result = float('inf')
        
        for i in range(len(values)-1):
            result = min(result, abs(values[i]-values[i+1]))
            
        return result