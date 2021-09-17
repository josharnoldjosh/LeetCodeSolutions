class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        graph = {i: idx+1
                 for idx, i in enumerate(sorted(set(arr)))}
        return [graph[i] 
                for i in arr]