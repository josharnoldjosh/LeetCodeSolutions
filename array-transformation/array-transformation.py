class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        
        def next_day(arr):
            result = [arr[0]]            
            for i in range(1, len(arr)-1):
                a, b, c = arr[i-1], arr[i], arr[i+1]                
                if a > b < c:
                    result += [b+1]
                elif a < b > c:
                    result += [b-1]
                else:
                    result += [b]
            result += [arr[-1]]
            return result
        
        
        
        curr = None
        
        while curr != arr:
            arr, curr = next_day(arr), arr
            
        return arr