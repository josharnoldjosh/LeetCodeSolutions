class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        items = (collections.Counter(nums1) & collections.Counter(nums2)).items()
        for k, v in items:
            result += [k]*v
        return result
