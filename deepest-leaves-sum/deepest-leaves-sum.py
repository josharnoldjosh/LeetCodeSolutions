# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
                                                        
        sums = collections.defaultdict(int)
                
        def recurse(node, depth):
            if not node: return 0            
            sums[depth] += node.val
            return max(
                depth,
                recurse(node.left, depth+1),
                recurse(node.right, depth+1),                
            )
                       
        return sums[recurse(root, 0)]
    
"""
- find depth, then bfs and sum bottom row
    - saves memory
    
- dictionary, map depth to sum
    - O(n) space and time...
"""