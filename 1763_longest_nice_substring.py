class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ''

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                substring = s[i:j + 1]

                for ch in set(substring):
                    if ch.lower() in substring and ch.upper() in substring:
                        continue
                    else:
                        break
                else:
                    if len(substring) > len(ans):
                        ans = substring

        return ans
