class Solution:
    def countAndSay(self, n: int) -> str:           
        ans = "1"
        
        for _ in range(n-1):
            ans = "".join([f"{len(list(group))}{digit}" for digit, group in itertools.groupby(ans)])
            
        return ans
