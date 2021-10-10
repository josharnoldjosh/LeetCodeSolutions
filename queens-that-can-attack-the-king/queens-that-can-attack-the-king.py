class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        """
        Expand out from the kings direction until we hit a queen or a wall.
        """
        def expand(start, direction):
            if (
                not (0 <= start[0] < 8) or
                not (0 <= start[1] < 8)
            ):
                return None
            if start in queens:
                return start
            return (
                expand(
                    [sum(x) for x in zip(*[start, direction])],
                    direction
                )
            )
        
        result = []
        for direction in [
            (0, 1), (0, -1),
            (1, 0), (-1, 0),
            (1, 1), (-1, -1),
            (-1, 1), (1, -1)
        ]:
            queen = expand(king, direction)
            if queen:
                result += [queen]
                
        return result