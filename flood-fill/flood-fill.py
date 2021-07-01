class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        seen = set()
        
        def recurse(i, j, c):
            seen.add((i, j))
            if not (0 <= i < len(image)): return
            if not (0 <= j < len(image[0])): return
            if image[i][j] != c: return
            image[i][j] = newColor
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (i+di, j+dj) in seen: continue
                recurse(i+di, j+dj, c)
                
        recurse(sr, sc, image[sr][sc])
                    
        return image
        