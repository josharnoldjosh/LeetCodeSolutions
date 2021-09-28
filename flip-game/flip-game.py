class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        
        def flip(currentState, idx):
            return "".join([
                c
                if jdx not in {idx, idx+1}
                else '-'
                for jdx, c in enumerate(currentState)
            ])
        
        return [
            flip(currentState, idx)
            for idx in range(len(currentState)-1)
            if currentState[idx:idx+2] == "++"
        ]
            