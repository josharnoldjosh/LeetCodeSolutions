class Codec:
    def serialize(self, root):                        
        def preorder(node):
            if not node: return "#"
            return f"{node.val} {preorder(node.left)} {preorder(node.right)}"                    
        return preorder(root)        
            
    def deserialize(self, data):        
        
        def build(vals):
            node = next(vals)
            if node == "#":
                return None
            tree = TreeNode(node)
            tree.left = build(vals)
            tree.right = build(vals)
            return tree
        
        vals = iter(data.split())        
        return build(vals)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


"""
"""






