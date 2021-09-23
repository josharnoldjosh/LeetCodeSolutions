class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        transform_1 = "".join([
            str(ord(c) - ord('a') + 1)
            for c in s
        ])
                
        transform_n = transform_1
        for _ in range(k):
            transform_n = sum([int(c) for c in str(transform_n)])
            
        return transform_n