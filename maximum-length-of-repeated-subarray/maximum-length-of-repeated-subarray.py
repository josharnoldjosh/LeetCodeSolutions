class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
            
        A = "".join(map(chr, A))
        B = "".join(map(chr, B))
        
        for window in range(len(A)+1):
            if not any(A[i:i+window] in B for i in range(len(A) - window + 1)):
                return window-1
            
        return window