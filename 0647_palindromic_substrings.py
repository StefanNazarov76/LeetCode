class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                sub = s[i:j + 1]

                if sub == sub[::-1]:
                    ans += 1

        return ans
