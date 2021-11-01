class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(i) for i in s.split() if i.isnumeric()]
        return numbers == sorted(set(numbers))