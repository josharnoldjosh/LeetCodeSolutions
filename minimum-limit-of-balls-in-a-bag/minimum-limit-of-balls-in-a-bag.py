from math import ceil


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        
        def can_we_divide_entire_nums_array_less_than_max_ops(denominator):            
            num_operations = 0
            for i in nums:                
                num_operations += ceil(i/denominator)-1
            return num_operations <= maxOperations
        
        
        def binary_search_min_denominator():
            l, r = 1, max(nums)
            
            while l < r:
                mid = (l+r) // 2
                if can_we_divide_entire_nums_array_less_than_max_ops(mid):
                    """
                    Shift r down to see if we can find an even smaller denominator
                    """
                    r = mid
                else:
                    """
                    We cannot use "mid" as a denominator, because it requires too many operations, so
                    shift l up and try larger denominator.
                    """
                    l = mid+1            
            return l
        
        
        return binary_search_min_denominator()
    
        