class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        d = {}

        for i, x in enumerate(s):
            if x not in d:
                d[x] = i
            else:
                ans = max(ans, i - d[x] - 1)

        return ans