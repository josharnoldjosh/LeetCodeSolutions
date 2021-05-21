# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:        
                                            
        queue, graph = collections.deque([(root, 0)]), collections.defaultdict(list)
        
        while queue:
            node, depth = queue.popleft()
            if not node: continue
            graph[depth] += [node]
            queue.extend([
                (node.left, depth+1),
                (node.right, depth+1),
            ])
            
        levels = set(graph[max(graph.keys())])
     
        def node_contains_all_levels(node):
            if not node: return 0
            return (node in levels) + node_contains_all_levels(node.left) + node_contains_all_levels(node.right)
        
        queue, result = collections.deque([root]), None
        
        while queue:
            node = queue.popleft()
            if not node: continue
            if node_contains_all_levels(node) == len(levels):
                result = node
            queue.extend([node.left, node.right])
            
        return result
            
        
    
    
"""
In a "human" language perspective
- Find all nodes at deepest "level"
- union the node's together until you reach a single parent
- This is hard to write in code

Can we think of "top down" approach where we don't need to do this union type behavior.


- If a node has the same "depth" on left and right, it could be good.

- Just need to do BFS..? to ensure last node we reach satisfies this...

"""