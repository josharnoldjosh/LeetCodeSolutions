class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:        
        return [x[-1] for x in list(sorted([(sum(i), idx) for idx, i in enumerate(mat)]))][:k]
        