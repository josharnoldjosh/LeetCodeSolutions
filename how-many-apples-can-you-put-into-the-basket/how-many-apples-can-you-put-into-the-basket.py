class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        result = list(itertools.accumulate([0]+arr))
        return len([
            i
            for i in result   
            if i <= 5000
        ]) - 1