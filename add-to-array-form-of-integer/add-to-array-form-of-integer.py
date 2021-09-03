class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = int("".join([str(c) for c in num]))
        num += k
        return [c for c in str(num)]