class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def can_divide(num):
            digits = [int(c) for c in str(num)]
            if 0 in digits:
                return False
            return all(
                num % i == 0
                for i in digits
            )
        
        return [
            i
            for i in range(left, right+1)
            if can_divide(i)
        ]