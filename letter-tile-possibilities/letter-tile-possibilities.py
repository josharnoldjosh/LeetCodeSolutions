class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        result = set()
        
        for i in range(len(tiles)+1):
            for j in itertools.permutations(tiles, i):
                result.add(j)
        
        return len(result)-1