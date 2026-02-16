class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        last = '0'

        for d in target:
            if d != last:
                ans += 1
                last = d

        return ans
