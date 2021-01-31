
class Solution:
    
    def exist(self, board, word):               
        for i in range(len(board)):
            for j in range(len(board[0])):                
                if self.dfs(board, i, j, word):
                    return True                    
        return False
    
    
    def dfs(self, board, i, j, word):                
        
        if not board[i][j] == word[0]:
            return False
        
        if len(word) == 1:
            return True        
        
        board[i][j] = "#"
        
        for a, b in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if not (0 <= a < len(board) and 0 <= b < len(board[0])): continue
            if self.dfs(board, a, b, word[1:]): return True            
            
        board[i][j] = word[0]
        
        return False
        