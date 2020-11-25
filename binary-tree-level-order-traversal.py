class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        result = collections.defaultdict(list)
        
        queue = collections.deque([(root, 0)])
        
        while queue:            
            node, idx = queue.popleft()
            if not node: continue
            result[idx].append(node.val)
            queue.append((node.left, idx+1))
            queue.append((node.right, idx+1))
            
        return result.values()
