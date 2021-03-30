# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        result = []
        
        queue = collections.deque([(root,)])
        
        while queue:            
            nodes = queue.popleft()                            
            if not nodes: continue
            result.append(statistics.mean([i.val for i in nodes]))
            queue.append([j for i in nodes for j in (i.left, i.right) if j])
        
        return result