class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        result, prefix = 0, [0]+list(itertools.accumulate(arr))
                    
        for i in range(1, len(prefix)):            
            for j in range(i):
                if (i+j) % 2 == 0: continue
                result += prefix[i] - prefix[j]
                            
        return result
