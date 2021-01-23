class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        look_up = set(jewels)
        try:
            return sum([1 for s in stones if s in look_up])
        except:
            return 0
            
        
