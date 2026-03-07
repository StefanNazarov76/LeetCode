class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1

        for ch in set(s):
            l = s.find(ch)
            r = s.rfind(ch)

            ans = max(r - l - 1, ans)

        return ans
