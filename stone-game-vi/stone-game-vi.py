class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        A = sorted(zip(aliceValues, bobValues), key=sum)
        cmp = lambda x, y: 1 if x > y else (-1 if x < y else 0)
        return cmp(sum(a for a, b in A[::-2]), sum(b for a, b in A[-2::-2]))                
        
