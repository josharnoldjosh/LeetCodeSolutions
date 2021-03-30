class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        result, level = [], (root,)
        
        while level:
            result += [sum(i.val for i in level) / len(level)]
            level = [child for node in level for child in (node.left, node.right) if child]
            
        return result