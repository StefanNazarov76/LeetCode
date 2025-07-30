class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = 0
        for i, d in enumerate(a[::-1]):
            int_a += int(d) * (2 ** i)

        int_b = 0
        for i, d in enumerate(b[::-1]):
            int_b += int(d) * (2 ** i)

        return bin(int_a + int_b)[2:]
