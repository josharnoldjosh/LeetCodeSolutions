from collections import Counter

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        counts = Counter([x for i, j in logs for x in list(range(i, j))])
                
        val = counts.most_common(1)[0][1]
        
        result = sorted([i for i in counts.items() if i[1] == val])
        
        return result[0][0]