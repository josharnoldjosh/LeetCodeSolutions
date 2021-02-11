class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:    
        
                     
        @functools.lru_cache(None)
        def backtrack(i, j, path):
            
            # terminate
            if i not in range(0, len(board)): return
            if j not in range(0, len(board[0])): return
            if board[i][j] == "#": return
            
            # success
            path += board[i][j]
            if path in self.words:
                self.result.add(path)
                
            # backtrack
            c = board[i][j]
            board[i][j] = "#"
            
            for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                backtrack(x, y, path)
            
            board[i][j] = c
            
    
    
        self.words = set(words)
        self.result = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i, j, "")        
        
        return self.result