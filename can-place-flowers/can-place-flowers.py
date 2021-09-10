class Solution:
    def canPlaceFlowers(self, A: List[int], n: int) -> bool:
        
        A = [0] + A + [0]
        
        shards = [len(j) for j in "".join([str(i) for i in A]).split("1") if len(j) >= 3]
        
        def transform(x):
            if x < 3:
                return 0
            if x % 2 == 0:
                return (x - 1) // 2
            else:
                return x // 2
                
        
        return sum([transform(i) for i in shards]) >= n
        
"""
zeros   score
1       0
2       0
3       1
4       1
5       2
6       2
7       3
8       3
9       4
"""

