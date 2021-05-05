class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def recurse(node):
            if not node: return
            recurse(node.left)
            node.left = None
            self.cur.right = node
            self.cur = self.cur.right
            recurse(node.right)
            
        ans = self.cur = TreeNode(None)
        recurse(root)
        return ans.right
                