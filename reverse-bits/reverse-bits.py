class Solution:
    def reverseBits(self, n: int) -> int:
        data = str(bin(n))[2:][::-1]
        data = data + (32 - len(data)) * "0"        
        return int(data, 2)
