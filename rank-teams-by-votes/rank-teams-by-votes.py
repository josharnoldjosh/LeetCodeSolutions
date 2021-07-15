from functools import cmp_to_key
from collections import Counter, defaultdict


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        counts = defaultdict(Counter)
        for i in votes:
            for jdx, j in enumerate(i):
                counts[jdx][j] += 1
        
        def custom_sort(a, b):            
            for i in range(len(votes[0])):                     
                if counts[i][a] > counts[i][b]:
                    return 1
                elif counts[i][a] < counts[i][b]:
                    return -1            
            return 1 if f"{a}{b}" == "".join(sorted(a+b)) else -1
        
        result = votes[0]        
        result = sorted(result, key = cmp_to_key(custom_sort), reverse=True)
        return "".join(result)
                