class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            result.append(max([-1]+arr[i+1:]))
        return result
            
        