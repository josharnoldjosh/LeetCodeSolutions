class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        if rowIndex == 2: return [1, 2, 1]
        
        result = [1]
        prevRow = self.getRow(rowIndex-1)
        for i in range(rowIndex):
            result += [sum(prevRow[i:i+2])]
        return result
            
        
        