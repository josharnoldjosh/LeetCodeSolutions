class Solution:
    def findComplement(self, num: int) -> int:
        return int(
            "".join([
                    '0' 
                    if c == '1' 
                    else '1' 
                    for c in str(bin(num))[2:]
                ]), 
            2)
        