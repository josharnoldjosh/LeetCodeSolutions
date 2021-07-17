class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:       
        prefix = list(itertools.accumulate([0]+arr))        
        result = 0        
        is_odd = lambda x: x % 2 != 0        
        even = [i for i in prefix if not is_odd(i)]
        odd = [i for i in prefix if is_odd(i)]        
        result = len(even) * len(odd)                                                
        return result % ((10 ** 9) + 7)