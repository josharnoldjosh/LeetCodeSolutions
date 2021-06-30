class Solution:
    def maxPower(self, s: str) -> int:
        
        best_streak = 0        
        cur_streak = 1
        x = ''        
        for c in s:
            if c == x:
                cur_streak += 1
            else:
                x = c
                cur_streak = 1
            best_streak = max(best_streak, cur_streak)
            
        
        return best_streak