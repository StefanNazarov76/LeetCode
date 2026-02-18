class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]

        return not '11' in b and not '00' in b
