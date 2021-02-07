"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            if not node: continue
                
            if queue and queue[0][1] == level:
                node.next = queue[0][0]
                
            queue.extend([
                (node.left, level+1),
                (node.right, level+1)
            ])
            print(node.val)
            
        return root
            
    
    
"""
Queue, BFS
Just check if next node is same level? then set to next? 

"""