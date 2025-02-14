class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[:2]

        for i in range(2, len(s)):
            if not (s[i] == ans[-2] and s[i] == ans[-1]):
                ans += s[i]

        return ans
