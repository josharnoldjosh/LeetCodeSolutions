class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
        
        i = j = k
        result = A[k]
        current_min = float('inf')
        
        while i > 0 or j < len(A)-1:
            
            if (A[i -1] if i > 0 else 0) < (A[j+1] if j < len(A)-1 else 0):
                j += 1
            else:
                i -= 1
                                
            current_min = min(current_min, A[i], A[j])
            result = max(result, current_min * (j - i + 1))
        
        return result
            
    