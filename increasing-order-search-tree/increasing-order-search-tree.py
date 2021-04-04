class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
                        
        global result
        result = dummy = TreeNode(0)
            
        def recurse(node):
            global result
            if not node: return
            recurse(node.left)
            result.right = TreeNode(node.val)
            result = result.right
            recurse(node.right)
                     
        recurse(root)        
        return dummy.right