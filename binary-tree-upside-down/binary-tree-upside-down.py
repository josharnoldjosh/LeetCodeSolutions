class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Termination Condition
        if not root or (not root.left and not root.right):
            return root
        
        # The original left child becomes the new root.
        left = self.upsideDownBinaryTree(root.left)
        
        # The original right child becomes the new left child.
        root.left.left = root.right
        
        # The original root becomes the new right child.
        root.left.right = root
        
        root.left = None
        root.right = None
        
        # The original left child becomes the new root.
        return left