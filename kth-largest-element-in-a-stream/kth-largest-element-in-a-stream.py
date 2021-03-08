class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)        

    def add(self, val: int) -> int:
        bisect.insort_left(self.nums, val, lo=0, hi=len(self.nums))
        return self.nums[-self.k]

        