class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
                        
        partition_len = len(nums) // k        
                
        @functools.lru_cache(maxsize=None)
        def recurse(nums):            
            if not nums: return 0
            
            result = float('inf')
            
            for combo in itertools.combinations(nums, partition_len):                
                
                # Stop duplicates
                if len(set(combo)) < partition_len: continue
                                 
                # "Remove" numbers in combo from nums
                updated_nums = list(nums) 
                for i in combo: updated_nums.remove(i)
                    
                # Recurse
                result = min(
                    result,
                    max(combo) - min(combo) + recurse(tuple(updated_nums))
                )
                
            return result
        
        result = recurse(tuple(nums))
        
        return result if result != float('inf') else -1
        
        
