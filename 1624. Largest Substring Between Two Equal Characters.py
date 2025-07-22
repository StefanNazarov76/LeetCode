class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1

        for ch in set(s):
            ans = max(s.rfind(ch) - s.find(ch) - 1, ans)

        return ans
