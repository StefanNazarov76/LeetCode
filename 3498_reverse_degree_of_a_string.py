class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s):
            ans += (26 - (ord(ch) - 97)) * (i + 1)

        return ans
