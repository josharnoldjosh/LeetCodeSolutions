class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:                
        x = [len(list(group)) for c, group in itertools.groupby(s)]
        y = list(itertools.accumulate([0]+x))
        data = [[i[-1], i[1]+i[0]-1] for i in zip(x, y) if i[0] >= 3]                
        return data