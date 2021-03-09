class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        counts = collections.Counter()
        
        def dfs(node):
            if not node: return 0            
            result = node.val + dfs(node.left) + dfs(node.right)
            counts[result] += 1        
            return result
        
        dfs(root)       
        
        try:
            freq = counts.most_common(1)[0][1]
            return [x[0] for x in counts.items() if x[1] == freq]
        except:
            return []
                        
