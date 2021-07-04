# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
                        
        def contains_node(root, node):
            if not all((root, node)): return False
            if root == node: return True            
            return contains_node(root.left, node) \
                or contains_node(root.right, node)
            
        result = []
            
        queue = collections.deque([(0, root)])
        
        while queue:
            depth, node = queue.popleft()
            if not node: continue
            if not (contains_node(node, p) and contains_node(node, q)):
                continue
            heapq.heappush(result, (depth, node))
            queue.extend([
                (depth-1, node.left),
                (depth-1, node.right),
            ])
            
        return heapq.heappop(result)[1] if result else None