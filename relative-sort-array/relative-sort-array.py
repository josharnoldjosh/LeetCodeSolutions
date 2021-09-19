class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        def sort(x):
            try:
                return arr2.index(x)
            except:
                return len(arr2) + x - 1
            
        arr1.sort(key = sort)
        
        return arr1