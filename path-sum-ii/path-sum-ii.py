# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        result = []
        
        def sink(node, target, path):            
            if not node: return
            if node.left == None and node.right == None and node.val == target:
                path+=[node.val]
                result.append(path)
            sink(node.right, target-node.val, path+[node.val])
            sink(node.left, target-node.val, path+[node.val])                
        
        sink(root, targetSum, [])
                
        return result