class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        def has_change(i):
            nonlocal counts
            if i == 5:
                return True
            elif i == 10:
                if counts[5]:
                    counts[5] -= 1
                    return True
            elif i == 20:
                if counts[5] >= 1 and counts[10]:
                    counts[5] -= 1
                    counts[10] -= 1
                    return True
                elif counts[5] >= 3:
                    counts[5] -= 3
                    return True                
            return False
                            
        counts = collections.Counter()
            
        for i in bills:
            counts[i] += 1
            if not has_change(i):
                return False
            
        return True
        
        