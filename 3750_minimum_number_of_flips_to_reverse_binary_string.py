class Solution:
    def minimumFlips(self, n: int) -> int:
        binary = bin(n)[2:]
        ans = 0

        for a, b in zip(binary, reversed(binary)):
            if a != b:
                ans += 1

        return ans
