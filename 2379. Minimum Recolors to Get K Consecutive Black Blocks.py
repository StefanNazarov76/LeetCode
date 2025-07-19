class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k

        for i in range(len(blocks) - k + 1):
            ans = min(ans, blocks[i:i + k].count('W'))

        return ans
