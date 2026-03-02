class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = '0'

        for _ in range(n - 1):
            inverted = ''.join('1' if c == '0' else '0' for c in ans)
            ans += '1' + inverted[::-1]

        return ans[k - 1]
