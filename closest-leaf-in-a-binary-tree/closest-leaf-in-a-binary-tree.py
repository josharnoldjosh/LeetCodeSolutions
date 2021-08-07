class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
            
        graph, leafs = collections.defaultdict(list), set()
            
        def make_graph(node):
            if not node:
                return
            if not(node.left or node.right):
                leafs.add(node.val)
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                make_graph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                make_graph(node.right)
                                     
        make_graph(root)
        
        queue, seen = collections.deque([k]), set()
        while queue:
            key = queue.popleft()
            if key in seen:
                continue
            seen.add(key)
            if key in leafs:
                return key
            queue.extend(graph[key])
            