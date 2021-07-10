class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for c in moves:
            x += 1 if c == "R" else 0            
            x -= 1 if c == "L" else 0
            y += 1 if c == "U" else 0
            y -= 1 if c == "D" else 0
        return (x, y) == (0, 0)