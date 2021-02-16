from collections import Counter

class Solution:
    
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        i_1, i_2 = Counter(i**2 for i in nums1), Counter(i**2 for i in nums2)
        
        f = lambda i, nums: sum(i[nums[j]*nums[k]] for j in range(len(nums)) for k in range(j+1, len(nums)))
         
        return f(i_1, nums2) + f(i_2, nums1)