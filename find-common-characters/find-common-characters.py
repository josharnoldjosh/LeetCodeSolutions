from collections import Counter
from functools import reduce

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        results = reduce(lambda x, y: x & y, [Counter(i) for i in A])
        return [j for i in results.items() for j in [i[0]] * i[1]]
        