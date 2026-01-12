class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0

        for i, ch in enumerate(s):
            ans += abs(i - t.index(ch))

        return ans
