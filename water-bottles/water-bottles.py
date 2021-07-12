class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
                        
        full, empty, tick = numBottles, 0, 0
        
        while full:
            tick += 1
            full -= 1
            empty += 1
            if empty ==  numExchange:
                empty = 0
                full += 1
                
        return tick
                
                
                