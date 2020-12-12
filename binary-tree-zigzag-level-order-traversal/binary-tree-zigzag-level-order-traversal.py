class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        
        result, queue = collections.defaultdict(list), collections.deque([(root, 0)])
        
        while queue:
            node, idx = queue.popleft()
            if not node: continue
            result[idx].append(node.val)
            queue.extend([(node.left, idx+1), (node.right, idx+1)])
            
        for idx in range(len(result.keys())):
            if idx % 2 == 0: continue
            result[idx].reverse()
            
        return result.values()
