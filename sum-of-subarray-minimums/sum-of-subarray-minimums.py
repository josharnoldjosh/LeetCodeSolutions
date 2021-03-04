class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
                 
        MOD = 10**9 + 7
        
        arr = [0] + arr + [0]
        
        stack = []        
        result = 0
        
        for idx, i in enumerate(arr):
            
            while stack and arr[stack[-1]] > i:
                jdx = stack.pop()
                kdx = stack[-1]
                result += arr[jdx] * (idx - jdx) * (jdx - kdx)
                
            stack.append(idx)
        
        return result % MOD