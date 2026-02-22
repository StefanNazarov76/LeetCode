class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1
        ans = 0

        for i, bit in enumerate(bin(n)[2:]):
            if bit == '1':
                if prev != -1:
                    ans = max(ans, i - prev)
                prev = i

        return ans
