class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return ''

        s_set = set(s)
        i = 0
        is_broken = False

        while i < n:
            if (s[i].islower() and s[i].swapcase() in s_set) or (s[i].isupper() and s[i].swapcase() in s_set):
                pass
            else:
                is_broken = True
                break
            i += 1

        if not is_broken:
            return s

        substr1 = self.longestNiceSubstring(s[:i])
        substr2 = self.longestNiceSubstring(s[i + 1:])

        return max(substr1, substr2, key=len)
