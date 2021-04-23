class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse=True)
        result = 0
        while costs:
            c = costs.pop()
            if c <= coins:
                coins -= c
                result += 1
            else:
                return result
        return result