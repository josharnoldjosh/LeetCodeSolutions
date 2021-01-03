class Solution:
    def letterCombinations(self, digits: str) -> List[str]:        
        
        ans = []
        graph = {'2':"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}          
        data = [graph[d] for d in digits]        
        queue = collections.deque([("", 0)])
        
        while queue:
            
            s, i = queue.popleft()
            
            if i == len(digits):
                ans.append(s)
                continue
                
            for c in data[i]:
                queue.append((s+c, i+1))
                                
        return ans if ans != [""] else []
