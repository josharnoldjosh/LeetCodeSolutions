class Solution:
    
    def validCounts(self, row):        
        counts = collections.Counter(row)
        try: del counts["."]
        except: pass
        try:
            return counts.most_common(1)[0][1] <=1
        except: return True
    
    def validate_square(self, board, i, j):
        row = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
        return self.validCounts(row)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        result = True
        
        board_t = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
        
        # Rows & Columns
        for idx in range(len(board)):
            result = all((result, self.validCounts(board[idx]), self.validCounts(board_t[idx])))
        
        # Squares
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                result = all((result, self.validate_square(board, i, j)))
                                        
        return result
        
